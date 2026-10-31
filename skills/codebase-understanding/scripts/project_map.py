#!/usr/bin/env python3
"""Optional, local project map. Python AST, Markdown links, JS imports and #include.
No project execution, network, dependency installation or persistent background work.
"""
import argparse
import ast
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import stat
from datetime import datetime, timezone
import tempfile

SCHEMA = 'local-project-map/1'
EXCLUDED = {'.git', 'node_modules', '.venv', 'venv', '__pycache__', '.project-map'}
TEXT = {'.py', '.md', '.markdown', '.js', '.jsx', '.jsxinc', '.ts', '.tsx', '.mjs', '.cjs'}
LIMIT = 1024 * 1024


def digest(data):
    return hashlib.sha256(data).hexdigest()


def engine_id():
    return digest(Path(__file__).read_bytes())


def inventory(root, map_path):
    records, content, skipped = {}, {}, []
    def walk_error(exc):
        name = os.path.relpath(exc.filename or root, root)
        skipped.append({'path': name, 'reason': 'walk-error:' + type(exc).__name__})
    for directory, dirs, files in os.walk(root, followlinks=False, onerror=walk_error):
        here = Path(directory)
        for name in sorted(list(dirs)):
            path = here / name
            if name in EXCLUDED or path.is_symlink():
                dirs.remove(name)
                skipped.append({'path': path.relative_to(root).as_posix(), 'reason': 'excluded-directory-or-symlink'})
        dirs.sort()
        for name in sorted(files):
            p = here / name
            if p == map_path:
                continue
            rel = p.relative_to(root).as_posix()
            try:
                mode = p.lstat().st_mode
            except OSError as exc:
                records[rel] = {'status': 'error', 'reason': type(exc).__name__}
                continue
            if not stat.S_ISREG(mode) or p.is_symlink() or name.startswith('.env') or p.suffix.lower() in {'.pem', '.key', '.p12'}:
                records[rel] = {'status': 'skipped', 'reason': 'symlink-or-sensitive-name'}
                continue
            try:
                h = hashlib.sha256()
                chunks, size = [], 0
                with p.open('rb') as f:
                    while chunk := f.read(65536):
                        h.update(chunk)
                        size += len(chunk)
                        if size <= LIMIT:
                            chunks.append(chunk)
                record = {'sha256': h.hexdigest(), 'bytes': size, 'status': 'file-only'}
                if size > LIMIT:
                    record.update(status='unsupported', reason='over-1MiB-parse-limit')
                else:
                    data = b''.join(chunks)
                    try:
                        text = data.decode('utf-8')
                        if '\x00' in text:
                            raise UnicodeError('NUL/binary')
                        content[rel] = text
                        if p.suffix.lower() not in TEXT:
                            record.update(status='unsupported', reason='no-structural-parser')
                    except UnicodeError:
                        record.update(status='unsupported', reason='binary-or-non-UTF8')
                records[rel] = record
            except OSError as exc:
                records[rel] = {'status': 'error', 'reason': type(exc).__name__}
    return records, content, skipped


def git_state(root):
    def run(*args):
        result = subprocess.run(['git', '--no-optional-locks', '-c', 'core.fsmonitor=false', '-c', 'core.hooksPath=/dev/null', '-C', str(root), *args], capture_output=True, text=True, timeout=5)
        return result.stdout.strip() if result.returncode == 0 else None
    try:
        return {'head': run('rev-parse', 'HEAD'), 'status': run('status', '--porcelain', '--untracked-files=all')}
    except (OSError, subprocess.TimeoutExpired):
        return {'head': None, 'status': None}


def build(root, map_path):
    root, map_path = root.resolve(), map_path.resolve()
    records, texts, skipped = inventory(root, map_path)
    nodes, edges, trees, symbols = {}, [], {}, {}

    def node(ident, kind, name, path, line=1):
        nodes.setdefault(ident, {'id': ident, 'kind': kind, 'name': name, 'path': path, 'line': line, 'certainty': 'candidate' if kind in {'heading', 'unresolved-file', 'external-module'} else 'syntax'})
        return ident

    def edge(src, dst, kind, path, line, certainty='syntax', detail=''):
        # Append, never key by unordered endpoints. Preserve type, direction and occurrence.
        edges.append({'id': f'e{len(edges)}', 'source': src, 'target': dst, 'type': kind,
                      'evidence': {'path': path, 'line': line}, 'certainty': certainty, 'detail': detail})

    for rel in records:
        node('file:' + rel, 'file', rel, rel)
    for rel, text in texts.items():
        if Path(rel).suffix.lower() == '.py':
            try:
                tree = ast.parse(text, filename=rel)
                trees[rel] = tree
                records[rel]['status'] = 'parsed'
                class Definitions(ast.NodeVisitor):
                    def __init__(self):
                        self.stack = []
                    def define(self, n):
                        qual = '.'.join(self.stack + [n.name])
                        ident = 'symbol:' + rel + ':' + qual + ':' + str(n.lineno)
                        node(ident, 'class' if isinstance(n, ast.ClassDef) else 'function', qual, rel, n.lineno)
                        symbols.setdefault((rel, qual), []).append(ident)
                        edge('file:' + rel, ident, 'contains', rel, n.lineno)
                        self.stack.append(n.name)
                        self.generic_visit(n)
                        self.stack.pop()
                    visit_FunctionDef = define
                    visit_AsyncFunctionDef = define
                    visit_ClassDef = define
                Definitions().visit(tree)
            except (SyntaxError, RecursionError, MemoryError) as exc:
                trees.pop(rel, None)
                for key in [k for k in symbols if k[0] == rel]:
                    symbols.pop(key)
                for ident in [i for i, n in nodes.items() if n['path'] == rel and n['kind'] != 'file']:
                    nodes.pop(ident)
                edges[:] = [e for e in edges if e['evidence']['path'] != rel]
                records[rel].update(status='error', reason='python-' + type(exc).__name__, line=getattr(exc, 'lineno', None))
        elif Path(rel).suffix.lower() in {'.md', '.markdown'}:
            records[rel]['status'] = 'partial'
            records[rel]['reason'] = 'headings-and-inline-local-links-only'
            for line, value in enumerate(text.splitlines(), 1):
                if re.match(r'^#{1,6}\s', value):
                    title = value.lstrip('#').strip()
                    ident = node('heading:' + rel + ':' + str(line), 'heading', title, rel, line)
                    edge('file:' + rel, ident, 'contains', rel, line, 'candidate', 'lexical heading; fences/frontmatter not resolved')
                for match in re.finditer(r'\[[^\]]*\]\(([^\s)]+)\)', value):
                    target = match[1].split('#', 1)[0]
                    if not target or re.match(r'[\w+.-]+:', target):
                        records[rel].setdefault('omitted_relations', []).append({'line': line, 'reason': 'empty-anchor-or-external-URI'})
                        continue
                    resolved = (root / rel).parent / target
                    try:
                        dest = resolved.resolve().relative_to(root).as_posix()
                    except ValueError:
                        records[rel].setdefault('omitted_relations', []).append({'line': line, 'reason': 'outside-root-link'})
                        continue
                    ident = node('file:' + dest, 'file' if dest in records else 'unresolved-file', dest, dest)
                    edge('file:' + rel, ident, 'document-link', rel, line, 'candidate', 'lexical link; fenced examples may match')
        elif Path(rel).suffix.lower() in {'.js', '.jsx', '.jsxinc', '.ts', '.tsx', '.mjs', '.cjs'}:
            records[rel].update(status='partial', reason='literal-includes-and-imports-only; no-JS-call-resolution')
            for line, value in enumerate(text.splitlines(), 1):
                include = re.match(r'^\s*#include\s+["<]([^">]+)[">]', value)
                imports = re.match(r'^\s*(?:import\s+.*?from\s*|export\s+.*?from\s*|import\s*)[\'\"]([^\'\"]+)[\'\"]', value)
                match = include or imports
                if match:
                    name = match[1]
                    if include or name.startswith('.'):
                        dest = os.path.normpath(str(Path(rel).parent / name)).replace(os.sep, '/')
                        if dest.startswith('../') or Path(dest).is_absolute():
                            records[rel].setdefault('omitted_relations', []).append({'line': line, 'reason': 'outside-root-include-or-import'})
                            continue
                        ident = node('file:' + dest, 'file' if dest in records else 'unresolved-file', dest, dest)
                    else:
                        ident = node('external:' + name, 'external-module', name, rel, line)
                    edge('file:' + rel, ident, 'includes' if include else 'imports', rel, line,
                         'candidate', 'lexical candidate; comments/template literals/conditional code not resolved')

    modules = {}
    for rel in trees:
        module = rel[:-3].replace('/', '.')
        if module.endswith('.__init__'):
            module = module[:-9]
        modules[module] = rel
    for rel, tree in trees.items():
        aliases = {}
        for n in ast.walk(tree):
            if isinstance(n, (ast.Import, ast.ImportFrom)):
                if isinstance(n, ast.Import):
                    items = [(a.name, '', a.asname or a.name.split('.')[0]) for a in n.names]
                else:
                    package = rel.split('/')[:-1]
                    if n.level:
                        base = package[:len(package) - n.level + 1]
                        prefix = '.'.join(base + ([n.module] if n.module else []))
                    else:
                        prefix = n.module or ''
                    items = [(prefix, a.name, a.asname or a.name) for a in n.names]
                for module, member, alias in items:
                    name = module + ('.' + member if member else '')
                    ident = node('import:' + name, 'import-name', name, rel, n.lineno)
                    edge('file:' + rel, ident, 'imports', rel, n.lineno)
                    target_rel = modules.get(module) or modules.get(name)
                    if target_rel:
                        edge('file:' + rel, 'file:' + target_rel, 'import-candidate', rel, n.lineno,
                             'candidate', 'local module path; runtime import resolution not established')
                        aliases[alias] = (target_rel, member if module in modules else '')
        class Calls(ast.NodeVisitor):
            def __init__(self):
                self.stack = []
                self.owners = []
            def function(self, n):
                self.stack.append(n.name)
                self.owners.append('symbol:' + rel + ':' + '.'.join(self.stack) + ':' + str(n.lineno))
                self.generic_visit(n)
                self.owners.pop()
                self.stack.pop()
            visit_FunctionDef = function
            visit_AsyncFunctionDef = function
            visit_ClassDef = function
            def visit_Call(self, n):
                owner = self.owners[-1] if self.owners else 'file:' + rel
                if isinstance(n.func, ast.Name):
                    name = n.func.id
                    candidates = list(symbols.get((rel, name), []))
                    if name in aliases:
                        path, symbol = aliases[name]
                        candidates += symbols.get((path, symbol), [])
                elif isinstance(n.func, ast.Attribute) and isinstance(n.func.value, ast.Name) and n.func.value.id in aliases:
                    path, _ = aliases[n.func.value.id]
                    candidates = symbols.get((path, n.func.attr), [])
                else:
                    candidates = []
                for ident in candidates:
                    edge(owner, ident, 'calls-candidate', rel, n.lineno, 'candidate',
                         'syntax and name match; shadowing/dynamic binding not established')
                if not candidates:
                    records[rel].setdefault('unresolved_calls', []).append(n.lineno)
                self.generic_visit(n)
        Calls().visit(tree)
    after, _, after_skipped = inventory(root, map_path)
    stable = (records_identity(records) == records_identity(after) and skipped == after_skipped
              and not any(v['status'] == 'error' and 'sha256' not in v for v in records.values())
              and not any(v['reason'].startswith('walk-error') for v in skipped))
    return {'schema': SCHEMA, 'created_at': datetime.now(timezone.utc).isoformat(), 'engine': engine_id(), 'root': str(root), 'inventory': records,
            'skipped': skipped, 'git': git_state(root), 'stable_snapshot': stable,
            'nodes': list(nodes.values()), 'edges': edges,
            'limitations': ['Static navigation only; no absence-of-dependencies proof.',
                            'Python calls/import resolution are candidates, not runtime observations.',
                            'Markdown and JS parsers are lexical and incomplete; GDScript unsupported.']}


def records_identity(records):
    return {p: {k: v for k, v in r.items() if k in {'sha256', 'bytes'} or k == 'status' and 'sha256' not in r}
            for p, r in records.items()}


def freshness(graph, root, map_path):
    root, map_path = root.resolve(), map_path.resolve()
    now, texts, skipped = inventory(root, map_path)
    old = records_identity(graph['inventory'])
    new = records_identity(now)
    changes = {'added': sorted(new.keys() - old.keys()), 'deleted': sorted(old.keys() - new.keys()),
               'changed': sorted(p for p in new.keys() & old.keys() if new[p] != old[p])}
    fresh = not any(changes.values()) and graph.get('engine') == engine_id() and graph.get('stable_snapshot') and skipped == graph.get('skipped') and graph.get('root') == str(root)
    return bool(fresh), changes, now, texts, skipped


def source_search(texts, query):
    # Ordinary literal source search, including text in unsupported formats. No execution.
    for path, text in sorted(texts.items()):
        for line, value in enumerate(text.splitlines(), 1):
            if query.casefold() in value.casefold():
                yield {'path': path, 'line': line}


def bounded(result, budget):
    def size():
        return len(json.dumps(result, ensure_ascii=False).encode('utf-8')) + 1
    result['output_truncated'] = False
    # Coverage can dwarf the useful neighborhood. Summarize it first, explicitly.
    coverage = result.get('coverage')
    if size() > budget and isinstance(coverage, dict):
        gaps, files, skipped = coverage.get('gaps', []), coverage.get('files', {}), coverage.get('skipped', [])
        result['coverage'] = {'details_omitted': True, 'gap_count': len(gaps),
                              'file_count': len(files) if isinstance(files, dict) else files,
                              'skipped_count': len(skipped), 'complete_dependency_analysis': False,
                              'gap_sample': [{k: x[k] for k in ['path', 'status', 'reason'] if k in x} for x in gaps[:3]],
                              'skipped_sample': skipped[:3]}
        result['output_truncated'] = True
    lists = [('fallback', 'matches'), (None, 'edges'), (None, 'nodes')]
    while size() > budget:
        for parent, key in lists:
            owner = result.get(parent, {}) if parent else result
            if isinstance(owner.get(key), list) and owner[key]:
                owner[key].pop()
                result['output_truncated'] = True
                break
        else:
            # Keep the safety result even when a repository has a huge change/coverage inventory.
            for key in ['changes', 'coverage']:
                if isinstance(result.get(key), dict) and not result[key].get('minimal'):
                    result[key] = {'details_omitted': True, 'minimal': True, 'reason': 'output-byte-budget'}
                    result['output_truncated'] = True
                    break
            else:
                raise ValueError('Output metadata exceeds byte budget')
    return result


def query(graph, root, map_path, term, impact, limit, budget):
    fresh, changes, records, texts, current_skipped = freshness(graph, root, map_path)
    selected, links = [], []
    if fresh:
        selected = [n for n in graph['nodes'] if term.casefold() in (n['name'] + ' ' + n['path']).casefold()]
        ids = {n['id'] for n in selected}
        if impact:
            ids.update(n['id'] for n in graph['nodes'] if n['path'] in {v['path'] for v in selected})
            links = [e for e in graph['edges'] if e['target'] in ids]
        else:
            links = [e for e in graph['edges'] if e['source'] in ids or e['target'] in ids]
        neighbors = ids | {e['source'] for e in links} | {e['target'] for e in links}
        selected = [n for n in graph['nodes'] if n['id'] in neighbors]
    gaps = [{'path': p, 'status': v['status'], 'reason': v.get('reason', ''), 'unresolved_calls': v.get('unresolved_calls', [])}
            for p, v in (graph['inventory'] if fresh else records).items() if v['status'] != 'parsed' or v.get('unresolved_calls')]
    fallback = not fresh or not selected or bool(gaps) or bool(current_skipped) or any(e['certainty'] == 'candidate' for e in links)
    from itertools import islice
    found = list(islice(source_search(texts, term), limit + 1)) if fallback else []
    matches = found[:limit]
    chosen = selected[:limit]
    present = {n['id'] for n in chosen}
    chosen_links = [e for e in links if e['source'] in present and e['target'] in present][:limit]
    result = {'schema': SCHEMA, 'fresh': fresh, 'changes': changes, 'mode': 'potential-impact' if impact else 'search',
              'coverage': {'gaps': gaps, 'skipped': current_skipped, 'complete_dependency_analysis': False},
              'nodes': chosen, 'edges': chosen_links,
              'selection_truncated': len(selected) > limit or len(chosen_links) < len(links),
              'source_search_truncated': len(found) > limit,
              'fallback': {'required': fallback, 'performed': 'literal-source-search' if fallback else None,
                           'matches': matches, 'next': 'Inspect source evidence and use rg for wider/deeper search; graph absence proves nothing.'}}
    result = bounded(result, budget)
    present = {n['id'] for n in result['nodes']}
    kept = [e for e in result['edges'] if e['source'] in present and e['target'] in present]
    if len(kept) != len(result['edges']):
        result['output_truncated'] = True
        result['edges'] = kept
    return result


def save(graph, path, root):
    if path.suffix != '.json':
        raise ValueError('Map output must be .json')
    if path.exists():
        old = json.loads(path.read_text())
        if old.get('schema') != SCHEMA:
            raise ValueError('Refusing to overwrite an unrelated JSON file')
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix='.project-map-', suffix='.tmp', dir=path.parent)
    try:
        with os.fdopen(fd, 'w') as f:
            json.dump(graph, f, ensure_ascii=False)
            f.flush()
            os.fsync(f.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('operation', choices=['build', 'search', 'impact', 'status'])
    p.add_argument('root', type=Path)
    p.add_argument('--map', required=True, type=Path, help='Explicit local JSON map; prefer outside source tree')
    p.add_argument('--query', default='')
    p.add_argument('--limit', type=int, default=12)
    p.add_argument('--max-bytes', type=int, default=8192)
    args = p.parse_args()
    root, path = args.root.resolve(), args.map.resolve()
    if not root.is_dir() or not 1 <= args.limit <= 200 or not 2048 <= args.max_bytes <= 131072:
        p.error('Require directory root, limit 1..200, max-bytes 2048..131072')
    try:
        if args.operation == 'build':
            graph = build(root, path)
            candidate_only = not graph['stable_snapshot'] or any(v['status'] == 'error' for v in graph['inventory'].values())
            output = path.with_name(path.stem + '.candidate.json') if candidate_only else path
            save(graph, output, root)
            result = {'map': str(output), 'candidate_only': candidate_only, 'files': len(graph['inventory']), 'nodes': len(graph['nodes']),
                      'edges': len(graph['edges']), 'stable_snapshot': graph['stable_snapshot'],
                      'coverage_complete': False, 'coverage': {'gaps': [{'path': p, **v} for p, v in graph['inventory'].items() if v['status'] != 'parsed' or v.get('unresolved_calls')], 'skipped': graph['skipped']}, 'limitations': graph['limitations']}
            result = bounded(result, args.max_bytes)
        else:
            if not args.query and args.operation != 'status':
                p.error('Search/impact requires a nonempty literal --query')
            try:
                graph = json.loads(path.read_text())
                if graph.get('schema') != SCHEMA:
                    raise ValueError('Unsupported map schema')
                if args.operation == 'status':
                    fresh, changes, records, _, skipped = freshness(graph, root, path)
                    result = bounded({'fresh': fresh, 'changes': changes, 'coverage': {'files': graph['inventory'] if fresh else records, 'skipped': skipped}}, args.max_bytes)
                else:
                    result = query(graph, root, path, args.query, args.operation == 'impact', args.limit, args.max_bytes)
            except (OSError, ValueError, KeyError, TypeError, AttributeError, RecursionError) as exc:
                records, texts, skipped = inventory(root, path)
                found = list(__import__('itertools').islice(source_search(texts, args.query), args.limit + 1)) if args.query else []
                result = bounded({'fresh': False, 'map_error': type(exc).__name__, 'nodes': [], 'edges': [],
                                  'coverage': {'files': records, 'skipped': skipped},
                                  'source_search_truncated': len(found) > args.limit,
                                  'fallback': {'required': True, 'performed': 'literal-source-search',
                                               'matches': found[:args.limit],
                                               'next': 'Use rg and inspect original sources; rebuild map if useful.'}}, args.max_bytes)
        print(json.dumps(result, ensure_ascii=False))
        return 0 if result.get('fresh', result.get('stable_snapshot', False)) and not result.get('candidate_only') else 2
    except (OSError, ValueError) as exc:
        print(json.dumps({'error': type(exc).__name__, 'message': str(exc)[:240]}))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())

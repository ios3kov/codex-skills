#!/usr/bin/env python3
"""Check reference identities and media bytes; visual similarity needs inspection."""
import argparse
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

TRACKING = {'gclid', 'dclid', 'fbclid', 'msclkid', 'mc_cid', 'mc_eid'}

def canonical_url(value):
    parts = urlsplit(value.strip())
    if parts.scheme.lower() not in {'http', 'https'} or not parts.hostname:
        raise ValueError(f'Expected HTTP(S) URL: {value!r}')
    if parts.username or parts.password:
        raise ValueError('Source URLs must not contain credentials')
    host = parts.hostname.lower()
    if ':' in host:
        host = f'[{host}]'
    port = parts.port
    scheme = parts.scheme.lower()
    if port and not (scheme == 'http' and port == 80 or scheme == 'https' and port == 443):
        host += f':{port}'
    query = [(k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True)
             if not k.lower().startswith('utm_') and k.lower() not in TRACKING]
    # Preserve order for repeated keys and hash-router routes; they can select content.
    fragment = parts.fragment if parts.fragment.startswith(('/', '!')) else ''
    return urlunsplit((scheme, host, parts.path or '/',
                       urlencode(sorted(query, key=lambda pair: pair[0])), fragment))

def normalize_title(value):
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFKC', value).casefold()).strip()

def scan(current_path, history_paths):
    current_path = Path(current_path).resolve()
    paths = [current_path] + [Path(p).resolve() for p in history_paths]
    if len(set(paths)) != len(paths):
        raise ValueError('Each manifest must be supplied once; current is not history')
    identity_map, title_map = {}, {}
    duplicates, warnings, errors = [], [], []
    history_items = 0
    for manifest in paths:
        data = json.loads(manifest.read_text())
        items = data.get('items')
        if not isinstance(items, list):
            raise ValueError(f'Manifest items must be a list: {manifest}')
        if manifest != current_path:
            history_items += len(items)
        ids = set()
        for index, item in enumerate(items):
            item_id = item.get('id', f'item-{index + 1}')
            if item_id in ids:
                raise ValueError(f'Duplicate item id {item_id!r} in {manifest}')
            ids.add(item_id)
            owner = (str(manifest), item_id)
            keys = set()
            for field in ('sourceUrl', 'pageUrl', 'imageUrl'):
                if item.get(field):
                    keys.add(('url', canonical_url(item[field])))
            for asset in item.get('assets', []):
                local = (manifest.parent / asset['path']).resolve()
                if not local.is_relative_to(manifest.parent):
                    errors.append({'item': owner, 'reason': 'Asset escapes bundle folder', 'path': asset['path']})
                    continue
                if not local.is_file():
                    errors.append({'item': owner, 'reason': 'Missing asset', 'path': asset['path']})
                    continue
                digest = hashlib.sha256(local.read_bytes()).hexdigest()
                if asset.get('sha256') and digest != asset['sha256'].lower():
                    errors.append({'item': owner, 'reason': 'Asset hash mismatch', 'path': asset['path']})
                keys.add(('sha256', digest))
            for key in sorted(keys):
                for previous in identity_map.get(key, []):
                    if str(current_path) in (owner[0], previous[0]):
                        duplicates.append({'kind': key[0], 'value': key[1], 'items': [previous, owner]})
                identity_map.setdefault(key, []).append(owner)
            title = normalize_title(item.get('title', ''))
            if title:
                for previous in title_map.get(title, []):
                    if str(current_path) in (owner[0], previous[0]):
                        warnings.append({'reason': 'Common title needs review', 'title': title, 'items': [previous, owner]})
                title_map.setdefault(title, []).append(owner)
    return {'status': 'FAIL' if duplicates or errors else 'PASS',
            'identityScope': 'current-and-supplied-history' if history_paths else 'current-only',
            'historyManifestCount': len(history_paths), 'historyItemCount': history_items,
            'semanticVariety': 'NOT RUN', 'duplicateCount': len(duplicates),
            'duplicates': duplicates, 'warnings': warnings, 'errors': errors}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest', type=Path)
    parser.add_argument('--history', nargs='+', default=[], type=Path)
    args = parser.parse_args()
    try:
        result = scan(args.manifest, args.history)
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        print(json.dumps({'status': 'FAIL', 'error': str(exc)}, ensure_ascii=False))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['status'] == 'PASS' else 1

if __name__ == '__main__':
    sys.exit(main())

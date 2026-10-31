import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / 'project_map.py'
spec = importlib.util.spec_from_file_location('project_map', SCRIPT)
m = importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class Scenarios(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name).resolve();self.root = self.base/'repo';self.root.mkdir();self.map = self.base/'map.json'
    def write(self, name, text):
        p=self.root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text);return p
    def build(self):
        with patch('socket.socket', side_effect=AssertionError('Network forbidden')):
            g=m.build(self.root,self.map);m.save(g,self.map,self.root);return g
    def cli(self, op, *args, path=None):
        p=subprocess.run([sys.executable,str(SCRIPT),op,str(self.root),'--map',str(path or self.map),*args],capture_output=True,text=True)
        return p,json.loads(p.stdout)
    def test_real_build_search_and_reciprocal_calls(self):
        self.write('a.py','from b import beta\ndef alpha():\n    beta()\n')
        self.write('b.py','from a import alpha\ndef beta():\n    alpha()\n')
        p,g=self.cli('build');self.assertEqual(p.returncode,0)
        data=json.loads(self.map.read_text());calls=[e for e in data['edges'] if e['type']=='calls-candidate'];self.assertEqual(len(calls),2)
        self.assertEqual({(e['source'].split(':')[1],e['target'].split(':')[1]) for e in calls},{('a.py','b.py'),('b.py','a.py')})
        self.assertTrue(all(e['certainty']=='candidate' and e['evidence']['line']==3 for e in calls))
        p,r=self.cli('search','--query','alpha');self.assertTrue(r['fresh']);self.assertTrue(r['nodes']);self.assertTrue(r['edges'])
        p,r=self.cli('impact','--query','b.py');self.assertTrue(any(e['evidence']['path']=='a.py' for e in r['edges']))
    def test_missing_map_fallback_count_limit(self):
        self.write('many.py', 'needle = 1\n' * 20)
        p,r=self.cli('search','--query','needle','--limit','2')
        self.assertEqual(p.returncode,2);self.assertEqual(len(r['fallback']['matches']),2);self.assertTrue(r['source_search_truncated'])
    def test_multiple_relations_and_reciprocal_documents(self):
        self.write('a.jsx','#include "b.jsx"\nimport "./b.jsx";\n#include "b.jsx"\n')
        self.write('b.jsx','#include "a.jsx"\n')
        self.write('a.md','# A\n[B](b.md) [B again](b.md)\n');self.write('b.md','# B\n[A](a.md)\n')
        g=self.build();same=[e for e in g['edges'] if e['source']=='file:a.jsx' and e['target']=='file:b.jsx']
        self.assertEqual([e['type'] for e in same],['includes','imports','includes'])
        docs=[e for e in g['edges'] if e['type']=='document-link'];self.assertEqual(len(docs),3)
        self.assertEqual(len({e['id'] for e in g['edges']}),len(g['edges']))
        ids={n['id'] for n in g['nodes']};self.assertTrue(all(e['source'] in ids and e['target'] in ids and e['evidence']['line']>0 for e in g['edges']))
    def test_edit_delete_add_and_source_fallback(self):
        self.write('module.py','def before():\n    return 1\n');self.write('caller.py','from module import before\nbefore()\n');g=self.build()
        self.write('module.py','def after():\n    return 2\n');(self.root/'caller.py').unlink();self.write('new.py','after = 9\n')
        p,r=self.cli('search','--query','after');self.assertEqual(p.returncode,2);self.assertFalse(r['fresh']);self.assertEqual(r['nodes'],[])
        self.assertEqual(r['changes'],{'added':['new.py'],'deleted':['caller.py'],'changed':['module.py']})
        self.assertEqual({x['path'] for x in r['fallback']['matches']},{'module.py','new.py'})
        g2=self.build();self.assertNotIn('caller.py',g2['inventory']);self.assertFalse(any(n['name']=='before' for n in g2['nodes']))
    def test_yaml_only_same_size_same_mtime(self):
        p=self.write('SKILL.md','---\nname: alpha\n---\n# Same body\n');g=self.build();stamp=p.stat().st_mtime_ns
        p.write_text(p.read_text().replace('alpha','bravo'));os.utime(p,ns=(stamp,stamp));fresh,changes,*_=m.freshness(g,self.root,self.map)
        self.assertFalse(fresh);self.assertEqual(changes['changed'],['SKILL.md'])
    def test_unsupported_gd_and_extendscript(self):
        self.write('game.gd','func signal_ready():\n    pass\n');self.write('main.jsx','#include "common.jsxinc"\n');self.write('common.jsxinc','var value = 1;\n')
        g=self.build();self.assertEqual(g['inventory']['game.gd']['status'],'unsupported');self.assertTrue(any(e['type']=='includes' and e['target']=='file:common.jsxinc' for e in g['edges']))
        p,r=self.cli('search','--query','signal_ready');self.assertTrue(r['fallback']['required']);self.assertEqual(r['fallback']['matches'],[{'path':'game.gd','line':1}])
    def test_missing_corrupted_and_wrong_engine_maps(self):
        self.write('a.py','needle = 1\n')
        p,r=self.cli('search','--query','needle');self.assertEqual(p.returncode,2);self.assertTrue(r['fallback']['required'])
        self.map.write_text('{invalid');p,r=self.cli('search','--query','needle');self.assertEqual(r['fallback']['matches'][0]['line'],1)
        self.map.unlink();g=self.build();g['engine']='old';m.save(g,self.map,self.root);p,r=self.cli('search','--query','needle');self.assertFalse(r['fresh'])
    def test_dirty_git_and_untracked_bytes(self):
        def git(*args):subprocess.run(['git','-C',str(self.root),*args],check=True,capture_output=True)
        git('init');self.write('a.py','old = 1\n');git('add','.');git('-c','user.name=Fixture','-c','user.email=fixture@example.invalid','commit','-m','fixture')
        g=self.build();self.write('a.py','new = 2\n');self.write('untracked.md','# New\n');p,r=self.cli('status');self.assertFalse(r['fresh']);self.assertEqual(r['changes']['added'],['untracked.md']);self.assertEqual(r['changes']['changed'],['a.py'])
    def test_budget_skips_errors_and_no_execution(self):
        self.write('run.py','raise RuntimeError("MUST NOT EXECUTE")\n')
        self.write('bad.py','def broken(\n');self.write('.env','PRIVATE_KEY=secret\n');self.write('blob.bin','\x00needle\n')
        for i in range(70):self.write(f'docs/{i}.md','# needle '+('é'*120)+'\n')
        self.write('node_modules/ignored.js','needle\n');g=self.build();self.assertEqual(g['inventory']['bad.py']['status'],'error');self.assertEqual(g['inventory']['.env']['status'],'skipped')
        p,r=self.cli('search','--query','needle','--limit','200','--max-bytes','2048');self.assertLessEqual(len(p.stdout.encode()),2048);self.assertTrue(r['output_truncated']);self.assertTrue(r['fallback']['required']);self.assertNotIn('secret',p.stdout)
    def test_failed_build_preserves_previous_map(self):
        self.write('a.py','x=1\n');self.build();before=self.map.read_bytes();self.write('a.py','def bad(\n')
        p,r=self.cli('build');self.assertEqual(p.returncode,2);self.assertTrue(r['candidate_only']);self.assertEqual(self.map.read_bytes(),before)
        self.assertTrue(Path(r['map']).exists())
    def test_lexical_headings_are_not_syntax_facts(self):
        self.write('a.md','```python\n# Not a heading\n```\n')
        g=self.build();n=next(n for n in g['nodes'] if n['kind']=='heading');self.assertEqual(n['certainty'],'candidate')
        self.assertTrue(all(e['certainty']=='candidate' for e in g['edges'] if e['target']==n['id']))
    def test_new_exclusions_are_reported(self):
        self.write('a.py','needle = 1\n');self.build();self.write('node_modules/ignored.js','needle\n')
        p,r=self.cli('search','--query','needle');self.assertFalse(r['fresh']);self.assertTrue(any(x['path']=='node_modules' for x in r['coverage']['skipped']))
    def test_deep_ast_is_a_diagnostic_not_a_crash(self):
        self.write('a.py','x=1\n');self.build();before=self.map.read_bytes();self.write('deep.py','value = '+'+'.join(['1']*6000)+'\n')
        p,r=self.cli('build');self.assertEqual(p.returncode,2);self.assertTrue(r['candidate_only']);self.assertEqual(self.map.read_bytes(),before)
        g=json.loads(Path(r['map']).read_text());self.assertEqual(g['inventory']['deep.py']['status'],'error')
    def test_unreadable_directory_and_disappearing_file_are_reported(self):
        self.write('a.py','x=1\n');d=self.root/'private';d.mkdir();(d/'lost.py').write_text('x=2\n');d.chmod(0)
        try:
            if os.access(d,os.R_OK):self.skipTest('Host can read mode-000 directory')
            p,r=self.cli('build');self.assertEqual(p.returncode,2);g=json.loads(Path(r['map']).read_text());self.assertTrue(any(x['path']=='private' and x['reason'].startswith('walk-error') for x in g['skipped']))
        finally:d.chmod(0o700)
        victim=self.write('disappear.py','x=3\n');original=Path.lstat;hit=[]
        def racing(path,*args,**kwargs):
            if path==victim and not hit:
                hit.append(True);victim.unlink();raise FileNotFoundError('fixture race')
            return original(path,*args,**kwargs)
        with patch.object(Path,'lstat',racing):g=m.build(self.root,self.map)
        self.assertEqual(g['inventory']['disappear.py']['status'],'error');self.assertFalse(g['stable_snapshot'])
    def test_realistic_build_output_and_query_have_useful_bounded_context(self):
        for i in range(80):self.write(f'module{i}.py',f'def needle{i}():\n    external()\n')
        p,r=self.cli('build','--max-bytes','2048');self.assertEqual(p.returncode,0);self.assertLessEqual(len(p.stdout.encode()),2048)
        p,r=self.cli('search','--query','needle','--max-bytes','4096');self.assertTrue(r['nodes']);self.assertLessEqual(len(p.stdout.encode()),4096)
        present={n['id'] for n in r['nodes']};self.assertTrue(all(e['source'] in present and e['target'] in present for e in r['edges']))
    def test_redefined_functions_keep_the_lexical_caller(self):
        self.write('a.py','def target():\n    pass\ndef repeat():\n    target()\ndef repeat():\n    target()\n')
        g=self.build();edges=[e for e in g['edges'] if e['type']=='calls-candidate'];self.assertEqual({(e['source'],e['evidence']['line']) for e in edges},{('symbol:a.py:repeat:3',4),('symbol:a.py:repeat:5',6)})
    def test_no_unrelated_json_overwrite(self):
        self.write('a.py','x=1\n');self.map.write_text('{"user":"data"}');p,r=self.cli('build');self.assertEqual(p.returncode,2);self.assertEqual(json.loads(self.map.read_text()),{'user':'data'})

if __name__=='__main__':unittest.main(verbosity=2)

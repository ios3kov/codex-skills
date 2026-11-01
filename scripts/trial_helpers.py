"""Run owned offline CLI scenarios. This tests helpers, not model/skill effectiveness."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / 'skills/codebase-understanding/scripts/project_map.py'
PLAN = ROOT / 'skills/agent-orchestrator/scripts/validate_plan.py'


def run_trials():
    checks, executions = [], []
    with tempfile.TemporaryDirectory(prefix='skill-helper-trial-') as temporary:
        base = Path(temporary).resolve()
        project = base / 'project'
        project.mkdir()
        (project/'alpha.py').write_text('from beta import beta\ndef alpha():\n    return beta()\n')
        (project/'beta.py').write_text('from alpha import alpha\ndef beta():\n    return alpha()\n')
        skill = project/'SKILL.md'
        skill.write_text('---\nname: fixture\nversion: 1\n---\n# Fixture\n')
        (project/'game.gd').write_text('func unsupported_marker():\n    pass\n')
        graph_path = base/'map.json'

        def execute(helper, args, expected):
            result = subprocess.run([sys.executable, str(helper), *map(str,args)], cwd=base,
                                    text=True, capture_output=True, timeout=20)
            executions.append({'helper':str(helper.relative_to(ROOT)), 'args':[str(a).replace(str(base),'<fixture>') for a in args],
                               'exit':result.returncode,'stdout':result.stdout.replace(str(base),'<fixture>'),
                               'stderr':result.stderr.replace(str(base),'<fixture>')})
            if result.returncode != expected:
                raise RuntimeError('Unexpected helper exit: '+json.dumps(executions[-1]))
            return json.loads(result.stdout)

        def check(label, condition):
            if not condition:
                raise RuntimeError('Scenario failed: '+label)
            checks.append({'case':label,'status':'PASS'})

        result = execute(MAP, ['build',project,'--map',graph_path,'--max-bytes',16384], 0)
        graph = json.loads(graph_path.read_text())
        nodes = {node['id']:node for node in graph['nodes']}
        relations = {(nodes[e['source']]['name'],nodes[e['target']]['name']) for e in graph['edges'] if e['type']=='calls-candidate'}
        check('build preserves reciprocal call candidates with source evidence',
              {('alpha','beta'),('beta','alpha')} <= relations and all(e.get('evidence',{}).get('line',0)>0 and e['evidence'].get('path') for e in graph['edges']))
        check('unsupported format is reported, not silently treated as complete',
              graph['inventory']['game.gd']['status']!='parsed' and result['coverage_complete'] is False)
        result = execute(MAP,['search',project,'--map',graph_path,'--query','unsupported_marker','--max-bytes',2048],0)
        check('unsupported source can be found through literal fallback',
              result['fallback']['required'] and any(m['path']=='game.gd' for m in result['fallback']['matches']))
        skill.write_text(skill.read_text().replace('version: 1','version: 2'))
        result = execute(MAP,['status',project,'--map',graph_path,'--max-bytes',16384],2)
        check('frontmatter-only change makes the saved map stale','SKILL.md' in result['changes']['changed'] and result['fresh'] is False)
        result = execute(MAP,['search',project,'--map',graph_path,'--query','alpha','--max-bytes',2048],2)
        check('stale query uses bounded source fallback',result['fallback']['required'] and result['fallback']['performed']=='literal-source-search' and len(json.dumps(result,ensure_ascii=False).encode())<=2048)
        (project/'beta.py').unlink()
        execute(MAP,['build',project,'--map',graph_path,'--max-bytes',16384],0)
        graph = json.loads(graph_path.read_text())
        check('rebuild removes deleted file definitions','beta.py' not in graph['inventory'] and not any(n['kind']=='function' and n['path']=='beta.py' for n in graph['nodes']))
        tasks = [{'id':'inspect','reads':['src'],'writes':[],'acceptance':'Report source-linked dependencies'},
                 {'id':'repair','reads':['src'],'writes':['src/main.py'],'acceptance':'Fix the observed defect'}]
        plan_path = base/'plan.json'
        plan_path.write_text(json.dumps({'tasks':tasks}))
        result = execute(PLAN,[plan_path],2)
        check('unordered read/write conflict is rejected',not result['valid'] and any('conflict' in e for e in result['errors']))
        tasks[1]['depends_on']=['inspect']
        plan_path.write_text(json.dumps({'tasks':tasks}))
        result = execute(PLAN,[plan_path],0)
        check('explicit dependency permits the ordered plan',result['valid'] and not result['errors'])
    return {'status':'PASS','scope':'Eight owned offline helper CLI checks; no agents, models, simulator or media generation ran',
            'helper_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (MAP,PLAN)},
            'checks':checks,'executions':executions,'character_continuity_generation':'NOT RUN'}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path)
    args = parser.parse_args(argv)
    try:
        result = run_trials()
    except (OSError,ValueError,RuntimeError,subprocess.TimeoutExpired) as error:
        print(json.dumps({'status':'FAIL','error':str(error)}))
        return 1
    data = json.dumps(result,ensure_ascii=False,indent=2)+'\n'
    if args.out:
        args.out.write_text(data)
    print(json.dumps({'status':result['status'],'cases':len(result['checks']),'scope':result['scope']}))
    return 0


if __name__=='__main__':
    raise SystemExit(main())

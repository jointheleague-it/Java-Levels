from invoke import task
from pathlib import Path 
from textwrap import dedent
import shutil 
import yaml
import re
import html

repo_root = Path(__file__).parent


def compile_meta(level, metas):

    ld =  repo_root / 'lessons'


    print("Processing Level", level)


    lessons = {}

    for meta in metas:
       
        
        if meta['level'].lower() == level.lower():

            m, l, a = meta['module'], meta['lesson'], meta['assignment']

            if m not in lessons:
                lessons[m] = {}


            if l not in lessons[m]:
                lessons[m][l]= {}

            lessons[m][l][a]= meta

    return lessons


def indent_headings(t):

    lines = []

    for l in t.splitlines():
        if l.startswith('#'):
            l = "#"+l

        lines.append(l)

    return '\n'.join(lines)


def make_text(lv):

    
    first = list(lv.values())[0]

    if len(lv) == 1:
        return first['text']

    title = first['lesson'].replace('_',' ').title()

    o = f"# {title}\n\n"

    for ak, a in lv.items():
        
        o += indent_headings(a['text'])

    return o

@task
def make_lessons(ctx, level, meta_file):


    meta = yaml.safe_load(Path(meta_file).read_text())

    meta = compile_meta(level, meta)


    ld =  repo_root / 'lessons'


    lessons = {}

    lp = {
        'title': 'Java Levels',
        'description': 'All of the Java Levels',
        'pages':[],
        'resources':[],
        'sidebar': [],
        'lessons': None
    }


    for mk, mv in sorted(meta.items()):

        if not mk in lessons:
            lessons[mk] =  {
                'title': mk,
                'assignments':[]
            }

        for lk, lv in sorted(mv.items()):
            ltitle = (' '.join(lk.split('_')[1:])).title()
            print (mk, ltitle, len(lv))

            dir_ =  ld / mk / lk


            dir_.mkdir(parents=True, exist_ok=True)
            
            #(dir_/'.meta').write_text(yaml.dump(meta))

            text = make_text(lv)

            (dir_/'index.md').write_text(text)


            a = {
                'level': level, 
                'module': mk,
                'lesson': lk, 
                'title': ltitle,
                'description': ''
            }

            (dir_/'_assignment.yaml').write_text(yaml.dump(a))


            lessons[mk]['assignments'].append( str(dir_.relative_to(ld) ))
            lessons[mk]['assignments'] = list(sorted(lessons[mk]['assignments']))

    lp['lessons'] = lessons

    (ld / 'lesson-plan.yaml').write_text(yaml.safe_dump(lp))



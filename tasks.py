from invoke import task
from pathlib import Path 
from textwrap import dedent
import shutil 
import yaml
import re
import html

repo_root = Path(__file__).parent


def walk_asgn(root):

    root = Path(root)

    for f in root.glob('**/.meta'):
        yield f


def compile_meta(level, root):

    root = Path(root)

    ld =  repo_root / 'lessons'


    print("Processing Level", level)


    lessons = {}

    for mf in walk_asgn(root):

        meta = yaml.safe_load(mf.read_text())

        if meta['level'].lower() == level.lower():

            m, l, a = meta['module'], meta['lesson'], meta['assignment']

            if m not in lessons:
                lessons[m] = {}


            if l not in lessons[m]:
                lessons[m][l]= {}

            lessons[m][l][a]= meta

    return lessons

def make_text(ass):

    text = ''

    for k, v in sorted(ass.items()):
        
        title =  (' '.join(k.split('_')[1:])).title()
        text += f'\n# {title}\n\n'

        _, d = v['dir'].split('/src/')

        text += f" {{{{ javaref('{v['level']}','{v['module']}','{d}')  }}}} \n\n"  
        text += v['text']

    text = html.unescape(text)
    text = re.sub(r'\xa0', ' ', text)
    text = re.sub(r'</?div.*>', '', text)


    return text

@task
def make_lesson_dirs(ctx, level, root):

    ld =  repo_root / 'lessons'

    meta = compile_meta(level, root)

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



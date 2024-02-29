

from invoke import task
from pathlib import Path 
from textwrap import dedent
import shutil 
import yaml

repo_root = Path(__file__).parent


def get_lmla(dir_=None):
    """Get level, module, lesson, assignment from a directory"""
    if dir_ is None:
        p = Path('.')
    else:
        p = Path(dir_)

    parts = str(p.absolute()).split('/')

    l = None
    m = None
    ls = None
    a = None


    # The lesson is the first directory after 'src',
    # and the assignment is the directory after the lesson.

    for i, part in enumerate(parts):
        if part.startswith("Level"):
            l = part
        if part.startswith("Module"):
            m = part
        if part == "src":
            try:
                # The lesson must be a directory
                t = Path('/'.join(parts[:i + 1]))
                if t.is_dir():
                    ls = parts[i+1]
            except IndexError:
                pass
        if ls and parts[i] == ls:
            # The assignment must be a directory
            try:
                t = Path('/'.join(parts[:i+1]))
                if t.is_dir():
                    a = parts[i+1]
            except IndexError:
                pass

    return l, m, ls, a


@task
def make_lesson_dirs(ctx, level, root):

    root = Path(root)

    ld =  repo_root / 'lessons'

    print("Processing Level", level)


    for f in root.glob('**/.web'):


        f = f.parent

        try:
            l,m,ls,a = get_lmla(f)
        except Exception as e:
            print("ERROR (lmla) ", f, e)
            continue

        if l != level:
            continue


        if a is None and ls is None:
            # Module level
            print("No assignment ", f)
            continue

        elif a is None and ls is not None:
            # missing one level of less / assignment
            ls = ls.strip('_')
            a = ls
            assign = ls
        else:
            assign = ls.strip('_') +'_' + a.strip('_')


        dir_ = ld / l / m / assign

        ls = ls.strip('_')



        title = assign.replace('_', ' ').title()

        dir_.mkdir(parents=True, exist_ok=True)



        fm=f"# {title}"+"\n\n"


        src = (f/'.web'/'index.md')

        if src.exists():
            text = fm+ src.read_text()
        else:
            text = fm

        (dir_/'index.md').write_text(text)


        d = {
            'opath': str(f.relative_to(root)),
            'level': l,
            'module': m,
            'lesson': ls,
            'ossignment': a.strip('_'),
            'assignment': assign,
            'title': title,
            'description': ''

        }


        (dir_/'_assignment.yaml').write_text(yaml.dump(d))

        for e in f.iterdir():
            if e.is_file() and e.suffix in ('.png','.gif','.jpg'):
                shutil.copy(e, dir_/e.name)

@task
def make_lesson_plan(ctx):


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

    for f in ld.glob('**/_assignment.yaml'):

        dir_ = f.parent
        d = yaml.safe_load(f.read_text())
        m, l, a = d['module'], d['lesson'], d['assignment']

        if not m in lessons:
            lessons[m] =  {
                'title': m,
                'assignments':[]
            }

        p = f.parent.relative_to(ld)


        lessons[m]['assignments'].append( str(p ))

        lessons[m]['assignments'] = list(sorted(lessons[m]['assignments']))




    lp['lessons'] = lessons

    print(yaml.dump(lp))


 






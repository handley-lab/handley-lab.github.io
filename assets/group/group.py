import datetime
import yaml
import os

class Supervisor(object):
    def __init__(self, name, url=None):
        self.name = name
        self.url = url

    def __str__(self):
        if self.url is None:
            return self.name
        return f'<a href="{self.url}">{self.name}</a>'

supervisors = [
    Supervisor('Anthony Lasenby', "https://www.phy.cam.ac.uk/directory/lasenbya"),
    Supervisor('Mike Hobson', "https://www.phy.cam.ac.uk/directory/hobsonm"),
    Supervisor('Will Barker', "https://wevbarker.com/"),
    Supervisor('Eloy de Lera Acedo', "https://www.phy.cam.ac.uk/directory/dr-eloy-de-lera-acedo"),
    Supervisor('Anastasia Fialkov',"https://www.ast.cam.ac.uk/people/Anastasia.Fialkov"),
    Supervisor('Nima Razavi-Ghods', "https://www.phy.cam.ac.uk/staff/dr-nima-razavi-ghods"),
    Supervisor('Mark Ashdown', "https://www.phy.cam.ac.uk/staff/dr-mark-ashdown"),
    Supervisor('Keith Grainge', "https://www.research.manchester.ac.uk/portal/keith.grainge.html"),
    Supervisor('Malak Olamaie', "https://www.yorksj.ac.uk/our-staff/staff-profiles/malak-olamaie.php"),
    Supervisor('David Stefanyszyn',"https://www.nottingham.ac.uk/physics/people/david.stefanyszyn"),
    Supervisor('Suhail Dhawan',"https://www.lucy.cam.ac.uk/fellows/dr-suhail-dhawan"),
    Supervisor('Gábor Csányi',"http://www.eng.cam.ac.uk/profiles/gc121"),
    Supervisor('Harry Bevins',"https://harrybevins.co.uk/"),
]

supervisors = {s.name:s for s in supervisors}


class Level(object):
    def __init__(self, **kwargs):
        self.start = kwargs.pop('start')
        self.end = kwargs.pop('end', None)
        self.supervisors = [supervisors[s] for s in kwargs.pop('supervisors', [])]

    def __lt__(self, other):
        return self.seniority < other.seniority

    def to_dict(self):
        d = self.__dict__.copy()
        if not d['supervisors']:
            d.pop('supervisors')
        else:
            d['supervisors'] = [s.name for s in d['supervisors']]
        if d['end'] is None:
            d.pop('end')
        return d

    def __str__(self):
        return self.string


class PI(Level):
    key = 'pi'
    seniority = -1
    string = 'PI'

class PostDoc(Level):
    key = 'postdoc'
    seniority = 0
    string = 'Post-Doc'

class PhD(Level):
    key = 'phd'
    seniority = 1
    string = 'PhD student'

class MPhil(Level):
    key = 'mphil'
    seniority = 2
    string = 'MPhil student'

class PartIII(Level):
    key = 'partiii'
    seniority = 3
    string = 'Part III student' 

class Summer(Level):
    key = 'summer'
    seniority = 4
    string = 'Summer student'


levels = {p.key:p for p in [PI, PostDoc, PhD, MPhil, PartIII, Summer]}



class Student(object):
    def __init__(self, name, **kwargs):
        self.levels = [levels[level](**kwargs.pop(level)) for level in levels if level in kwargs]
        self.name = name
        self.email = kwargs.pop('email', None)
        self.original_image = kwargs.pop('original_image', None)
        self.image = kwargs.pop('image', None)
        self.links = kwargs.pop('links', None)
        self.destination =  kwargs.pop('destination', None) 

    def to_dict(self):
        d = self.__dict__.copy()
        d.pop('name')
        result = {}
        for level in sorted(d.pop('levels')):
            result[level.key] = level.to_dict()

        result.update({k: v for k, v in d.items() if v is not None})
        return result

    @property
    def start(self):
        return min([l.start for l in self.levels])

    def end(self):
        ends = [l.end for l in self.levels]
        if any([end==None for end in ends]):
            return None
        else:
            return max(ends)

    @property
    def seniority(self):
        return min(self.levels).seniority

    def __repr__(self):
        return self.name

    def __lt__(self, other):
        if self.seniority < other.seniority:
            return True
        elif self.seniority > other.seniority:
            return False
        else:
            return min(self.levels).start > min(other.levels).start

    def joint_papers(self):
        import arxiv
        arr = self.name.split(' ')
        surname = arr[-1]
        #initial = ','.join([section[0] for section in arr[0].split('-')])
        initial = arr[0][0]

        query = f'au:Handley_W AND au:{surname}_{initial}'
        query = query.replace('-','_')
        search = arxiv.Search(query=query)
        npapers = len(list(search.results()))

        if npapers>0:
            url = f'https://arxiv.org/search/?query=handley%2C+w%3B+{surname}%2C{initial}&searchtype=author'
            return f'<a href="{url}">Group research papers ({npapers})</a>'

yaml_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'group.yaml')

with open(yaml_file) as f:
    people = [Student(name, **kwargs) for name, kwargs in yaml.safe_load(f).items()]


people = sorted(people)

with open(yaml_file, 'w') as f:
    yaml.dump({p.name:p.to_dict() for p in people}, 
               f, default_flow_style=False, sort_keys=False)

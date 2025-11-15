import datetime
import yaml
import os
import re

class Level(object):
    def __init__(self, **kwargs):
        self.start = kwargs.pop('start', datetime.date(1970,1,1) )
        self.end = kwargs.pop('end', None)
        self.supervisors = kwargs.pop('supervisors', [])
        self.thesis = kwargs.pop('thesis', None)

    def __lt__(self, other):
        return self.seniority < other.seniority

    def to_dict(self):
        d = self.__dict__.copy()
        if not d['supervisors']:
            d.pop('supervisors')
        if d['end'] is None:
            d.pop('end')
        return d

    def __str__(self):
        return self.string


class PI(Level):
    key = 'pi'
    seniority = -1
    string = 'PI'

class CoI(Level):
    key = 'coi'
    seniority = -1
    string = 'Co-I'

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


levels = {p.key:p for p in [PI, CoI, PostDoc, PhD, MPhil, PartIII, Summer]}


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
        import yaml
        import re

        # Load papers.yaml - the ground truth
        papers_file = '../general/data/papers.yaml'
        try:
            with open(papers_file) as f:
                papers = yaml.safe_load(f)
        except FileNotFoundError:
            return None

        # Extract surname and first initial for matching
        name_parts = self.name.split(' ')
        surname = name_parts[-1].lower()
        first_initial = name_parts[0][0].lower()

        # Find papers where this person is an author
        person_papers = []
        for paper in papers:
            authors = paper.get('authors', [])
            # Join list of authors into a single string
            if isinstance(authors, list):
                authors_str = ' '.join(authors).lower()
            else:
                authors_str = str(authors).lower()

            # Use word boundary matching to avoid false positives
            # Match surname as a complete word (not substring)
            if re.search(r'\b' + re.escape(surname) + r'\b', authors_str):
                arxiv_id = paper.get('arxiv', '')
                title = paper.get('title', 'Untitled')
                if arxiv_id:
                    person_papers.append({'arxiv': arxiv_id, 'title': title})

        if len(person_papers) > 0:
            # Check if this is the PI - if so, just link to author page
            is_pi = any(isinstance(level, PI) for level in self.levels)

            if is_pi:
                # For PI, link to arXiv author page
                author_url = f'https://arxiv.org/a/{surname}_{first_initial}_1.html'
                return f'<a href="{author_url}">arXiv papers ({len(person_papers)})</a>'
            else:
                # For others, build HTML list of papers in reverse order (most recent first)
                html_list = '<ul>'
                for paper in reversed(person_papers):
                    arxiv_url = f"https://arxiv.org/abs/{paper['arxiv']}"
                    html_list += f'<li><a href="{arxiv_url}">{paper["title"]}</a></li>'
                html_list += '</ul>'
                return html_list

        return None

#yaml_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'group.yaml')
yaml_file = 'assets/group/group.yaml'

with open(yaml_file) as f:
    data = yaml.safe_load(f)

people = [Student(name, **kwargs) for name, kwargs in data.items()]
people = sorted(people)

supervisors = {name:list(d['links'].values())[0] for name, d in data.items() if 'coi' in d and 'links' in d}
supervisors

with open(yaml_file, 'w') as f:
    yaml.dump({p.name:p.to_dict() for p in people}, 
               f, default_flow_style=False, sort_keys=False)

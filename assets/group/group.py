import datetime
import html
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


def author_key(name):
    """(surname, first initial), accent- and case-insensitive; handles "Surname, First"."""
    import unicodedata
    if ',' in name:
        surname, first = name.split(',', 1)
        name = f'{first} {surname}'
    name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode()
    parts = re.sub(r'[^a-z ]', '', name.lower().replace('-', '')).split()
    return (parts[-1], parts[0][0]) if len(parts) > 1 else None


def paper_authors(paper):
    import ast
    authors = paper.get('authors') or []
    if isinstance(authors, str):
        try:
            authors = ast.literal_eval(authors)
        except (ValueError, SyntaxError):
            authors = [authors]
    return authors


def arxiv_date(arxiv_id):
    """First of the month an arXiv paper was submitted, from its new-style ID."""
    m = re.match(r'(\d\d)(\d\d)\.\d+', str(arxiv_id))
    return datetime.date(2000 + int(m.group(1)), int(m.group(2)), 1) if m else None


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

    def in_group_on(self, day):
        """True if day falls in any of this person's roles, plus a year after it ended."""
        grace = datetime.timedelta(days=365)
        return any(l.start <= day and (l.end is None or day <= l.end + grace) for l in self.levels)

    def postdoc_on(self, day):
        """True if day falls within one of this person's postdoc roles."""
        return any(isinstance(l, PostDoc) and l.start <= day and (l.end is None or day <= l.end)
                   for l in self.levels)

    def joint_papers(self):
        import yaml
        import re

        # Load papers.yaml - the ground truth
        papers_file = '../general/data/papers.yaml'
        try:
            with open(papers_file) as f:
                papers = yaml.safe_load(f)
        except FileNotFoundError:
            return self.cached_joint_papers()

        name_parts = self.name.split(' ')
        surname = name_parts[-1].lower()
        first_initial = name_parts[0][0].lower()

        # Group-paper rule (as for the map on /papers/, script/papers.py): the
        # paper must be from this person's time in the group (plus a year's
        # grace) and involve Will or another group member, except that a
        # postdoc's own papers while a postdoc always count. The PI's entry is
        # a link to their whole arXiv record, so it counts everything. Authors
        # match on surname and first initial, not surname alone.
        is_pi = any(isinstance(level, PI) for level in self.levels)
        me = author_key(self.name)
        others = {author_key(n) for n in data} - {me}
        person_papers = []
        for paper in papers:
            arxiv_id = paper.get('arxiv', '')
            keys = [author_key(a) for a in paper_authors(paper)]
            date = arxiv_date(arxiv_id)
            if not arxiv_id or me not in keys:
                continue
            if is_pi:
                person_papers.append({'arxiv': arxiv_id, 'title': paper.get('title', 'Untitled')})
                continue
            if date is None or not self.in_group_on(date):
                continue
            # A postdoc's own papers while here count as group output; anyone
            # else's need a second group author.
            if not self.postdoc_on(date) and not others.intersection(keys):
                continue
            person_papers.append({'arxiv': arxiv_id, 'title': paper.get('title', 'Untitled')})

        if len(person_papers) > 0:
            # The PI gets a link to their arXiv author page instead of a list
            if is_pi:
                # For PI, link to arXiv author page
                author_url = f'https://arxiv.org/a/{surname}_{first_initial}_1.html'
                return f'<a href="{author_url}">arXiv papers ({len(person_papers)})</a>'
            else:
                # For others, build HTML list of papers in reverse order (most recent first)
                html_list = '<ul>'
                for paper in reversed(person_papers):
                    arxiv_url = f"https://arxiv.org/abs/{paper['arxiv']}"
                    html_list += f'<li><a href="{arxiv_url}">{html.escape(paper["title"])}</a></li>'
                html_list += '</ul>'
                return html_list

        return None

    def cached_joint_papers(self):
        """Fallback when ../general/data/papers.yaml is absent: the snapshot in
        assets/group/joint_papers.yaml, rendered the same way."""
        try:
            with open('assets/group/joint_papers.yaml') as f:
                entry = (yaml.safe_load(f) or {}).get(self.name)
        except FileNotFoundError:
            return None
        if not entry:
            return None
        if isinstance(entry, dict):
            return f'<a href="{entry["author_page"]}">arXiv papers ({entry["count"]})</a>'
        html_list = '<ul>'
        for paper in entry:
            html_list += f'<li><a href="https://arxiv.org/abs/{paper["arxiv"]}">{html.escape(paper["title"])}</a></li>'
        return html_list + '</ul>'

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

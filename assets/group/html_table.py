#!/usr/bin/env python
from group import people, levels, supervisors
from yattag import Doc, indent
import os
from pandas import DataFrame, to_datetime
from datetime import datetime, date
df = DataFrame()
df['data'] = people
df['level'] = df.data.apply(lambda x: min(x.levels).key)
df['present'] = df.data.apply(lambda x: min(x.levels).start <= date.today() and (x.end()==None or x.end() >= date.today()))
df['future'] = df.data.apply(lambda x: min(x.levels).start > date.today()) 

html_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'group.html')

css = """
.grid{
  display: grid;
  gap: 1rem;
  grid-template-colums: repeat(1, 1fr);
  grid-template-columns: 100%;
}

.grid-item img {
   border-radius: 20%;
   width: 200px;
}

@media screen and (min-width: 600px){
   .grid{
      grid-template-colums: repeat(2, 1fr);
      grid-template-columns: 30% 70%;
   }
}
"""

ignore = ["George Carter", "Stephen Pickman", "Patrick Lau", "Samuel Hewson", "Nicolas Mediato Diaz", "Rose Luo", "Alex Drane", "Farah Wallauer", "Ajinkya Naik"]

with open(html_file, 'w') as f:
    doc = Doc()

    with doc.tag('style'):
        doc.asis(css)

    for i, df in enumerate([df[df.present], df[~df.present & ~df.future]]):
        for level in levels:
            if level == 'coi':
                continue
            sdf = df[df.level==level].data.to_list()
            if len(sdf):

                with doc.tag('div', klass='wrapper', style='margin-top:30pt'):
                    with doc.tag('h1'):
                        level_str = levels[level].string
                        if i==0:
                            if level_str == 'PI':
                                doc.text(f'{level_str}')
                            else:
                                doc.text(f'{level_str}s')
                        else:
                            doc.text(f'Past {level_str}s')
                    with doc.tag('div', klass="grid"):
                        for person in sdf:
                            if person.name in ignore:
                                continue
                            with doc.tag('div', klass="grid-item"):
                                if person.image:
                                    src = os.path.join('/assets/group/', person.image)
                                elif person.original_image:
                                    src = os.path.join('/assets/group/', person.original_image)
                                else:
                                    src = "/assets/images/user.png"
                                doc.stag('img', src=src)

                            with doc.tag('div', klass="grid-item"):
                                name = person.name
                                print(name)
                                with doc.tag('p'):
                                    with doc.tag('font', size="+2"):
                                        doc.text(name)
                                with doc.tag('p'):
                                    with doc.tag('ul'):
                                        for l in person.levels:
                                            with doc.tag('li'):
                                                doc.text(f'{l} from {l.start.strftime("%b %Y")}')
                                                if l.end:
                                                    doc.text(f' to {l.end.strftime("%b %Y")}')
                                                with doc.tag('ul'):
                                                    if l.supervisors:
                                                        text = []
                                                        for cs in l.supervisors:
                                                            if cs != 'Will Handley':
                                                                text.append(f'<a href="{supervisors[cs]}">{cs}</a>')
                                                        if text:  # Only display if there are co-supervisors
                                                            text = ', '.join(text)
                                                            with doc.tag('li'):
                                                                doc.asis(f"co-supervised with {text}")
                                                    if l.thesis:
                                                        doc.line('li', f'Thesis: {l.thesis}')

                                        joint_papers = person.joint_papers()
                                        if joint_papers:
                                            # Check if it's just a link (PI) or a full list (others)
                                            if joint_papers.startswith('<ul>'):
                                                doc.line('li', 'Group research papers:')
                                                doc.asis(joint_papers)
                                            else:
                                                with doc.tag('li'):
                                                    doc.asis(joint_papers)

                                        if person.links:
                                            doc.line('li', 'Links:')
                                            with doc.tag('ul'):
                                                for l, href in person.links.items():
                                                    with doc.tag('li'):
                                                        doc.asis(f"<a href='{href}'>{l}</a>")

                                        if person.destination:
                                            doc.line('li', 'Subsequent career:')
                                            with doc.tag('ul'):
                                                for date, loc in person.destination.items():
                                                    with doc.tag('li'):
                                                        doc.asis(f"{date.strftime('%b %Y')}: {loc}")

    f.write(indent(doc.getvalue()))

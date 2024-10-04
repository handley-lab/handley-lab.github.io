#!/usr/bin/env python
from group import people, levels
from yattag import Doc, indent
import os
from pandas import DataFrame, to_datetime
df = DataFrame()
df['data'] = people
df['level'] = df.data.apply(lambda x: min(x.levels).key)
df['present'] =  df.data.apply(lambda x: x.end()==None) 

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

ignore = ["George Carter", "Toby Lovick", "Stephen Pickman", "Patrick Lau", "Samuel Hewson", "Nicolas Mediato Diaz"]

with open(html_file, 'w') as f:
    doc = Doc()

    with doc.tag('style'):
        doc.asis(css)

    for i, df in enumerate([df[df.present], df[~df.present]]):
        for level in levels:
            sdf = df[df.level==level].data.to_list()
            if len(sdf):

                with doc.tag('div', klass='wrapper', style='margin-top:30pt'):
                    with doc.tag('h1'):
                        if i==0:
                            if levels[level].string == 'PI':
                                doc.text('%s' % levels[level].string)
                            else:
                                doc.text('%ss' % levels[level].string)
                        else:
                            doc.text('Past %ss' % levels[level].string)
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
                                                doc.text('%s from %s' % (l, l.start.strftime("%b %Y")))
                                                if l.end:
                                                    doc.text(' to %s' % l.end.strftime("%b %Y"))
                                                if l.supervisors:
                                                    str(l.supervisors[0])
                                                    with doc.tag('ul'):
                                                        with doc.tag('li'):
                                                            text = ', '.join([str(cs) for cs in  l.supervisors])
                                                            doc.asis("co-supervised with %s" % text)

                                        joint_papers = person.joint_papers()
                                        if joint_papers:
                                            with doc.tag('li'):
                                                doc.asis(joint_papers)

                                        if person.links:
                                            doc.line('li', 'Links:')
                                            with doc.tag('ul'):
                                                for l in person.links:
                                                    with doc.tag('li'):
                                                        doc.asis(l)

                                        if person.destination:
                                            doc.line('li', 'Subsequent career:')
                                            with doc.tag('ul'):
                                                for date, loc in person.destination.items():
                                                    with doc.tag('li'):
                                                        doc.asis("%s: %s" % (date.strftime("%b %Y"), loc))

    f.write(indent(doc.getvalue()))

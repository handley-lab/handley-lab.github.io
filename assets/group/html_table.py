#!/usr/bin/env python
"""Generate assets/group/group.html: one big card per person, in sections by
role (current members first, then past members), with filter chips.

Each person appears once, in the section for their most senior role, most
recent first. Styles live in _sass/minima/custom-styles.scss and the filter
script in _includes/group_cards.html.
"""
from group import people, levels, supervisors
from yattag import Doc, indent
import os
from datetime import date

html_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'group.html')

ignore = ["George Carter", "Stephen Pickman", "Patrick Lau", "Nicolas Mediato Diaz", "Ajinkya Naik"]

today = date.today()
sections = [key for key in levels if key != 'coi']


def status(person):
    if min(person.levels).start > today:
        return None
    end = person.end()
    return 'current' if end is None or end >= today else 'alumni'


def photo(person):
    if person.image:
        return person.image if person.image.startswith('http') else os.path.join('/assets/group/', person.image)
    if person.original_image:
        return os.path.join('/assets/group/', person.original_image)
    return "/assets/images/user.png"


def heading(level, state):
    name = levels[level].string
    if state == 'alumni':
        return f'Past {name}s'
    return name if level == 'pi' else f'{name}s'


doc, tag, text, line = Doc().ttl()

with tag('div', klass='group-filters', **{'aria-label': 'Filter group members'}):
    with tag('div', klass='group-filter-row', role='group', **{'aria-label': 'Current or past members'}):
        line('button', 'Current', type='button', klass='group-chip', **{'data-status': 'current', 'aria-pressed': 'true'})
        line('button', 'Past', type='button', klass='group-chip', **{'data-status': 'alumni', 'aria-pressed': 'false'})
    with tag('div', klass='group-filter-row', role='group', **{'aria-label': 'Role'}):
        line('button', 'Everyone', type='button', klass='group-chip', **{'data-role': 'all', 'aria-pressed': 'true'})
        for level in sections:
            label = levels[level].string + ('' if level == 'pi' else 's')
            line('button', label, type='button', klass='group-chip', **{'data-role': level, 'aria-pressed': 'false'})

for state in ['current', 'alumni']:
    for level in sections:
        members = [p for p in people
                   if p.name not in ignore and status(p) == state and min(p.levels).key == level]
        members.sort(key=lambda p: min(p.levels).start, reverse=True)
        if not members:
            continue
        with tag('section', klass='group-section', **{'data-status': state, 'data-role': level}):
            line('h2', heading(level, state))
            for person in members:
                with tag('article', klass='group-card'):
                    doc.stag('img', src=photo(person), alt=f'Photo of {person.name}', loading='lazy',
                             onerror="this.onerror=null;this.src='/assets/images/user.png'")
                    with tag('div', klass='group-card-body'):
                        line('h3', person.name)
                        with tag('ul'):
                            for l in sorted(person.levels, key=lambda l: l.start, reverse=True):
                                with tag('li'):
                                    text(f'{l} from {l.start.strftime("%b %Y")}')
                                    if l.end:
                                        text(f' to {l.end.strftime("%b %Y")}')
                                    cosup = [cs for cs in (l.supervisors or []) if cs != 'Will Handley']
                                    if cosup or l.thesis:
                                        with tag('ul'):
                                            if cosup:
                                                with tag('li'):
                                                    text('co-supervised with ')
                                                    for i, cs in enumerate(cosup):
                                                        if i:
                                                            text(', ')
                                                        if cs in supervisors:
                                                            line('a', cs, href=supervisors[cs])
                                                        else:
                                                            text(cs)
                                            if l.thesis:
                                                line('li', f'Thesis: {l.thesis}')

                            joint_papers = person.joint_papers()
                            if joint_papers:
                                # A plain link for the PI, a full list for everyone else
                                if joint_papers.startswith('<ul>'):
                                    line('li', 'Group research papers:')
                                    doc.asis(joint_papers)
                                else:
                                    with tag('li'):
                                        doc.asis(joint_papers)

                        links = {k: v for k, v in (person.links or {}).items() if v}
                        if links:
                            with tag('p', klass='group-card-links'):
                                for label, href in links.items():
                                    line('a', label, href=href)

                        if person.destination:
                            # Destinations may contain links, so insert them as HTML
                            line('p', 'Subsequent career:', klass='group-card-now')
                            with tag('ul', klass='group-card-career'):
                                for d, loc in person.destination.items():
                                    with tag('li'):
                                        doc.asis(f"{d.strftime('%b %Y')}: {loc}")

with open(html_file, 'w') as f:
    f.write(indent(doc.getvalue()))

# Homepage banner: every current member with a photo, shuffled and repeated to
# fill a tile wall (included by _layouts/landing.html).
import random
here = os.path.dirname(os.path.abspath(__file__))
faces = [os.path.join('/assets/group/', p.image) for p in people
         if p.name not in ignore and status(p) == 'current' and min(p.levels).key in sections
         and p.image and not p.image.startswith('http') and os.path.exists(os.path.join(here, p.image))]
tiles = []
rng = random.Random(0)
while len(tiles) < 72:
    batch = faces[:]
    rng.shuffle(batch)
    tiles += batch
doc, tag, text, line = Doc().ttl()
with tag('div', klass='group-collage-tiles', **{'aria-hidden': 'true'}):
    for src in tiles[:72]:
        doc.stag('img', src=src, alt='', loading='lazy')
with open(os.path.join(here, 'collage.html'), 'w') as f:
    f.write(indent(doc.getvalue()))
print(f'collage: {len(faces)} current members with photos')

#!/usr/bin/env python
from collections import Counter
from group import people
import matplotlib.pyplot as plt
import os
import datetime
import numpy as np
grey = '#bbbbbb'
plt.rcParams['axes.edgecolor'] = grey
plt.rcParams['xtick.color'] = grey
plt.rcParams['ytick.color'] = grey
plt.rcParams['ytick.color'] = grey
plt.rcParams['ytick.color'] = grey


people = [p for p in people if p.start <= datetime.date.today() and [l.key for l in p.levels] != ['coi']]
people = sorted(people, key=lambda p: (p.start, min([(l.start, l.seniority) for l in p.levels])[1]))

colors = {'partiii': 'C1',
          'phd': 'C0',
          'postdoc': 'C2',
          'summer': 'C3',
          'mphil': 'C4',
          'pi': 'C5'}

fig, ax = plt.subplots()
rects = {}
for i, person in enumerate(people):
    weight = None
    for l in person.levels:
        if l.key == 'coi':
            continue
        start = l.start.toordinal()
        if l.end is not None:
            end = l.end.toordinal() 
        else:
            end = datetime.date.today().toordinal()
        if end >= datetime.date.today().toordinal():
            weight = 'bold'
            
        rect = plt.Rectangle((start, i), end-start, 1, fc=colors[l.key], ec='k') 
        rects[str(l)] = rect
        ax.add_artist(rect)
    ax.annotate(person.name, (person.start.toordinal()-10, i+0.5), va='center', ha='right', color=grey, weight=weight)
        
min_year = min([person.start.year for person in people])
date_labels = [datetime.date(i,1,1) for i in range(min_year+1,datetime.date.today().year+2)]
xticks = [d.toordinal() for d in date_labels]
ax.set_xticks(xticks)
ax.set_xticklabels([d.year for d in date_labels])

ax.set_xlim(min([person.start.toordinal() for person in people])-400, datetime.date.today().toordinal())
ax.set_ylim(0,i+1)
ax.set_yticks([])

starts = np.array([(min([l.start.toordinal() for l in s.levels]), i) for i, s in enumerate(people)])
academic_date_labels = [datetime.date(i,10,1).toordinal() for i in range(min_year+1,datetime.date.today().year+2)]
for date in academic_date_labels:
    start = starts[starts[:,0] <= date][-1]
    line, = ax.plot([date, date], [0, start[1]], color=grey, linestyle=':', zorder=-1)

labels, handles  = np.transpose(list(rects.items()))
labels, handles = list(labels), list(handles)
labels += ['Academic Year']
handles += [line]
ax.legend(handles, labels, labelcolor=grey, framealpha=0.0)

png_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'group.png')

fig.set_size_inches(9,9)
fig.tight_layout()
fig.savefig(png_file, transparent=True)

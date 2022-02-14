from pprint import pprint
from collections import namedtuple
from prettytable import PrettyTable

pt = PrettyTable()
Anketa = namedtuple("Anketa", ['id', 'score', 'name', 'age'])
spis = []
file1 = open('profiles.dat', 'r')
Lines = file1.readlines()
i = 0
for line in Lines:
    i += 1
    if line != "":
        lst = line.split()
        spis.append(Anketa(lst[0], lst[1], lst[2], lst[3]))
spis_above_30 = []
for j, i in enumerate(spis):
    if int(i.score) >= 30:
        spis_above_30.append(i)
print(spis_above_30,"\n")
pprint(spis_above_30)
print("\n")
pt.field_names = ["ID", "SCORE", "NAME", "AGE"]
for i in spis_above_30:
    pt.add_row([i.id, i.score, i.name, i.age])
print(pt)

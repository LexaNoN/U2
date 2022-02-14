from pprint import pprint
from random import randint
import names
x = []
for i in range(100):
    x.append([i, randint(1, 100), names.get_first_name(), randint(10, 24)])
f = open("profiles.dat", "w")
for j in x:
    f.write(" ".join(map(str, j)) + "\n")
f.close()
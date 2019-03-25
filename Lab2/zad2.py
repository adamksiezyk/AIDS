import csv
import operator

f = open('zadanie2.csv', 'r')
t = f.read()
l = t.splitlines()
a = []
for word in l:
    if word[-1] == ',':
        a.append(word)

for word in a:
    l.remove(word)

i = 0
for k in l:
    rule = k.find(',')
    if rule == 3:
        l[i] = str('0') + k
    elif rule == 2:
        l[i] = str('00') + k
    elif rule == 1:
        l[i] = str('000') + k
    i += 1

l.sort()

for i in range(len(l)-1):
    if l[i][0:4] == l[i+1][0:4]:
        l[i+1].replace()
print l[-1]
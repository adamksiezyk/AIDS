import math
f = open('TSP.txt').readlines()
cities = []
for line in f:
    cities.append(line.split())

def Distance(a, b):
    return math.sqrt(math.pow(float(a[1])-float(b[1]),2) + math.pow(float(a[2])-float(b[2]), 2))

def Solution(a):
    p = 0
    visited = [a[0]]
    S = cities
    #del(S[a-1])
    temp = []
    for i in S:
        temp.append(Distance(a, i)
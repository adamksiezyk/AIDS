import math
f = open('TSP.txt').readlines()
cities = []
for line in f:
    cities.append(line.split())

def Distance(a, b):
    return math.sqrt(math.pow(float(cities[a][1])-float(cities[b][1]),2) + math.pow(float(cities[a][2])-float(cities[b][2]), 2))

def PathLength1(a):
    l = 0
    for i in range(a, len(cities)):
        l = l + Distance(i, (i+1)%len(cities))
    for i in range(a):
        l = l + Distance(i, (i+1)%len(cities))
    return l

def Solution(a):
    p = 0
    visited = [a]
    S = cities
    del(S[a-1])
    temp = []
    for i in S:
        temp.append(Distance(a-1, (int(i[0])-2)))


print PathLength1(20)
Solution(20)
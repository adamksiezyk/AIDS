f = open('packages100.txt').readlines()
t = f[2:len(f)]

elements = []
for line in t:
    elements.append(line.split(','))
s = 10
backpack = [[0 for j in range(s)] for i in range(s)]

def check(elem, x, y):
    global backpack
    l = int(elem[1])
    h = int(elem[2])
    for i in range(x+l):
        for j in range(y+h):
            if backpack[i][j] != 0:
                return False
    return True

def putin(elem):
    l = int(elem[1])
    h = int(elem[2])
    global backpack
    for y in range(s-h):
        for x in range(s-l):
            if check(elem, x, y):
                for i in range(l):
                    for j in range(h):
                        backpack[x+i][y+j] = int(elem[0])
    return

for e in elements:
    putin(e)

for i in backpack:
    print i
                    

    
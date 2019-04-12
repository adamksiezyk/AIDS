i = 0

def Hanoi(n, src, dest, buff):
    global i
    if n == 1:
        dest.append(src[-1])
        del(src[-1])
        i += 1
        print(i, )
        return
    Hanoi(n-1, src, buff, dest)
    dest.append(src[-1])
    del(src[-1])
    i += 1
    print(i)
    Hanoi(n-1, buff, dest, src)

s = [5,4,3,2,1]
d = []
b = []
Hanoi(len(s), s, d, b)
print(d)
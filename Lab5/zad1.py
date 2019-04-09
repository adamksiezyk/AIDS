i = 0

def Hanoi(n, src, dest, buff):
    global i
    if n == 1:
        dest.append(src[-1])
        del(src[-1])
        i += 1
        print(i)
        return
    Hanoi(n-1, src, buff, dest)
    dest.append(src[-1])
    del(src[-1])
    i += 1
    print(i)
    Hanoi(n-1, buff, dest, src)

s = [9,8,7,6,5]
d = []
b = []
Hanoi(5, s, d, b)
print(d)
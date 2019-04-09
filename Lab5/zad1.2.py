def check(src, dest):
    success = False
    if src != []:
        if dest == [] or src[-1] > dest[-1]:
            success = True
    return success

def Hanoi(src, dest, buff):
    while src != [] or buff != []:
        i = 1
        if i%3 == 1 and check(src, dest):
            dest.append(src[-1])
            del(src[-1])
        if i%3 == 2 and check(src, buff):
            buff.append(src[-1])
            del(src[-1])
        if i%3 == 0 and check(buff, dest):
            dest.append(buff[-1])
            del(buff[-1])
        i += 1

src = [5,6,7,8,9]
dest = []
buff = []
Hanoi(src, dest, buff)
print(dest)
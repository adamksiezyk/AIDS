def check(src, dest):
    success = False
    if src != []:
        if dest == [] or src[-1] < dest[-1]:
            success = True
    return success

def Hanoi(src, dest, buff):
    steps = 0
    i = 1
    while src != [] or buff != []:
        if i%3 == 1 :
            if check(src, dest):
                dest.append(src[-1])
                del(src[-1])
                steps += 1
                print(steps, src, buff, dest)
            elif check(dest, src):
                src.append(dest[-1])
                del(dest[-1])
                steps += 1
                print(steps, src, buff, dest)
        elif i%3 == 2:
            if check(src, buff):
                buff.append(src[-1])
                del(src[-1])
                steps += 1
                print(steps, src, buff, dest)
            elif check(buff, src):
                src.append(buff[-1])
                del (buff[-1])
                steps += 1
                print(steps, src, buff, dest)
        elif i%3 == 0:
            if check(buff, dest):
                dest.append(buff[-1])
                del(buff[-1])
                steps += 1
                print(steps, src, buff, dest)
            elif check(dest, buff):
                buff.append(dest[-1])
                del (dest[-1])
                steps += 1
                print(steps, src, buff, dest)
        i += 1

src = [5,4,3,2,1]
dest = []
buff = []
Hanoi(src, dest, buff)
import time

start_time = time.time()

file = open('zadanie2.csv', 'r')
sheet = file.read()
lines = sheet.splitlines()
id = []
val = []
dict = {}
for i in lines:
    i = i.split(',')
    if i[1] == '' or i[1] == '/n':
        pass
    else:
        id.append(i[0])
        i.remove(i[0])

        temp = ''
        for word in i:
            temp += word

        val.append(temp)



print(len(lines))
print(len(val))
print(len(id))
print(time.time()-start_time)
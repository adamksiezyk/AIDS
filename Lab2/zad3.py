import time

start = time.time()

file = open('SJP.txt').read()

while True:
    s = input('Wprowadź wyraz: ')
    if s.isalpha():
        break
    else:
        print('To nie wyraz!')

s = s.lower()

if s in file:
    print(s + ' jest słowem.')
else:
    print(s + ' nie jest słowem.')

end = time.time()
print(end - start)

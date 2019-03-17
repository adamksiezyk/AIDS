list = [[],[],[]]

for i in range(3):
    list[i].append(' ')
    list[i].append(' ')
    list[i].append(' ')

def prt():
    print(list[0])
    print(list[1])
    print(list[2])

def check():
    for row in range(3):
        rule1 = list[row][0]==list[row][1]==list[row][2]!=' '
        rule2 = list[0][row]==list[1][row]==list[2][row]!=' '
        rule3 = list[0][0]==list[1][1]==list[2][2]!=' '
        rule4 = list[2][0]==list[1][1]==list[0][2]!=' '
        if rule1 or rule2 or rule3 or rule4:
            print("Wygrana! Nowa gra?")
            a = input('T/N: ')
            if a == 'T':
                return 0

while True:
    for i in range(3):
        list[0][i] = ' '
        list[1][i] = ' '
        list[2][i] = ' '

    while True:
        prt()
        if check() == 0:
            break
        w = input("Podaj wiersz: ")
        k = input("Podaj kolumne: ")
        list[int(w)-1][int(k)-1] = 'O'
        prt()
        if check() == 0:
            break
        w = input("Podaj wiersz: ")
        k = input("Podaj kolumne: ")
        list[int(w)-1][int(k)-1] = 'X'
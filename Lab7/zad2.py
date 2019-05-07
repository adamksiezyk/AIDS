import time

f = open('3000_pattern.txt')
text = f.readlines()

# def sum(text):
#     n = len(text[0])
#     for i in range(0, n-2):
#         for j in range(0, n-2):
#             s = ord(text[i][j]) + ord(text[i][j+1]) + ord(text[i][j+2]) + ord(text[i+1][j]) + ord(text[i+2][j])
#             print(s)
#     return

# t=[['abc'],['bfc'],['chc']]
# sum(t)



def search(text):
    suma = 0
    length = ord('A') + ord('B')*2 + ord('C')*2
    n = len(text[0]) - 2
    for i in range(0, n-2):
        for j in range(0, n-2):
            value = ord(text[i][j]) + ord(text[i][j+1]) + ord(text[i][j+2]) + ord(text[i+1][j]) + ord(text[i+2][j])
            if value == length:
                if text[i][j] == 'A' and text[i+1][j] == 'B' and text[i+2][j] == 'C' and text[i][j+1] == 'B' and text[i][j+2] == 'C':
                    print str(i),',', str(j)
                    suma = suma + 1
    print(suma)                
    return

t1 = time.time()
search(text)
print time.time() - t1

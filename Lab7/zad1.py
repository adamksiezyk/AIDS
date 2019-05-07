import time

f = open('1000_pattern.txt')
text = f.readlines()

def search(text):
    n = len(text[0]) - 2
    for i in range(0,n-3):
        for j in range(0,n-3):
            if text[i][j] == 'A' and text[i+1][j] == 'B' and text[i+2][j] == 'C' and text[i][j+1] == 'B' and text[i][j+2] == 'C':
                print str(i),',', str(j)
    return

start = time.time()
search(text)
print(time.time() - start)
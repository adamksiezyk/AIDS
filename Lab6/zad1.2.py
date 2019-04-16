import zad1 as tree
import random

for i in range(10):
    tree.create(0.5 + i, i)
    tree.T.append(tree.V[i])
    print(tree.T[i])

for i in range(10, 20):
    tree.add(i-10+0.4, i)
    print(tree.T[i-10])

import time
import random

def insertionsort(A):
    for i in range(1, len(A)):
        x = A[i]
        j = i - 1
        while j >= 0 and A[j] > x:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = x
    return A

def merge(left, right):
    B = []
    while left and right:
        if left[0] <= right[0]:
            B.append(left[0])
            left = left[1:len(left)]
        else:
            B.append(right[0])
            right = right[1:len(right)]

    B.extend(left)
    B.extend(right)
    return B

def mergesort(A):
    length = len(A)
    if length <= 1:
        return A
    half = length/2
    sub1 = A[0:half]
    sub2 = A[half+1:length]
    sub1 = mergesort(sub1)
    sub2 = mergesort(sub2)
    return merge(sub1, sub2)

t1min = 1000
t2min = 1000
t1max = 0
t2max = 0
t1sum = 0
t2sum = 0

A = []
for j in range(0,10):
    for i in range(0, 1000):
        A.append(random.randint(1,5000))

    t11 = time.time()
    insertionsort(A)
    t12 = time.time()
    t1 = t12 - t11

    t21 = time.time()
    mergesort(A)
    t22 = time.time()
    t2 = t22 - t21

    if t1min > t1:
        t1min = t1
    if t1max < t1:
        t1max = t1

    if t2min > t2:
        t2min = t2
    if t2max < t2:
        t2max = t2

    t1sum += t1
    t2sum += t2

    j += 1

t1av = t1sum/10
t2av = t2sum/10

print('Insertsort: ')
print('min = ', t1min)
print('max = ', t1max)
print('suma = ', t1sum)
print('srednia = ', t1av)

print('Mergesort: ')
print('min = ', t2min)
print('max = ', t2max)
print('suma = ', t2sum)
print('srednia = ', t2av)

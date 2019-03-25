import random
import math
import time

start = time.time()

coord = []
for i in range(0, 1000):
    coord.append([random.uniform(0.0, 2.0), random.uniform(0.0, 1.0)])

hit = []

for point in coord:
    if point[1] <= math.sin(point[0]):
        hit.append(point)

print(len(hit)/2)

t = time.time() - start
print(t)
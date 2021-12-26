# https://www.codingame.com/ide/puzzle/rectangle-partition

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h, count_x, count_y = [int(i) for i in input().split()]
x, y=[0], [0]
for i in input().split():
    x.append(int(i))
x.append(w)
for i in input().split():
    y.append(int(i))
y.append(h)

from collections import Counter

d = Counter()
for i in range(len(y)):
    for j in range(i):
        d[y[i] - y[j]] += 1

n = 0
for i in range(len(x)):
    for j in range(i):
        n += d[x[i] - x[j]]
print(n)

lst = [True] * 10001
for i in range(1, 10001):
    n = i + sum(map(int, str(i)))
    if n <= 10000:
        lst[n] = False
for i in range(1, 10001):
    if lst[i]:
        print(i)

import sys
lst = [True] * 10001
for i in range(1, 9969):
    lst[i + sum(list(map(int, str(i))))] = False
for i in range(1, 9994):
    if lst[i]:
        print(i)
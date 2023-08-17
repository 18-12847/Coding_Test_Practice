import sys
from itertools import product
input = sys.stdin.readline
lst = [int(input().rstrip()) for _ in range(int(input().rstrip()))]
for i in lst:
    arr = [False, False] + [True] * (i - 1)
    for j in range(2, int(i ** 0.5) + 1):
        for k in range(j + j, i + 1, j):
            arr[k] = False
    for l in product([idx for idx, val in enumerate(arr) if val], repeat = 3):
        if sum(l) == i:
            print(*l)
            break
    else:
        print(0)
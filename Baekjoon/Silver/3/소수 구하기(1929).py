import sys
input = sys.stdin.readline
n, m  = map(int, input().split())
lst = [False, False] + [True] * (m - 1)
for i in range(2, int(m ** 0.5) + 1):
    for j in range(i + i, m + 1, i):
        lst[j] = False
for i in range(n, m + 1):
    if lst[i]:
        print(i)
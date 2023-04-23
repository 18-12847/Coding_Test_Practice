import sys
n, t ,c, p = map(int, sys.stdin.readline().split())
tot = 0
for i in range(1, n + 1 - t, t):
    tot += c
print(tot * p)
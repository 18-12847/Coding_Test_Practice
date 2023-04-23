import sys
n, m = map(int, sys.stdin.readline().split())
lst = [0] * n
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    for j in range(a, b + 1):
        lst[j-1] = c
print(*lst)
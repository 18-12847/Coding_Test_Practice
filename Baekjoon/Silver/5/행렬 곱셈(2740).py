import sys
n, m = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
m, k = map(int, sys.stdin.readline().split())
b = [list(map(int, sys.stdin.readline().split())) for i in range(m)]
for x in range(n):
    for y in range(k):
        tot = 0
        for z in range(m):
            tot += a[x][z] * b[z][y]
        print(tot, end = " ")
    print()
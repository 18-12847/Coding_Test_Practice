#Tlqkf
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst = [input().rstrip() for _ in range(n)]
tot = 1
for i in range(n):
    for j in range(m):
        cm = min(n-i, m-j)
        while cm > 1:
            if lst[i][j] == lst[i+cm-1][j] == lst[i][j+cm-1] == lst[i+cm-1][j+cm-1]:
                tot = max(tot, cm)
                break
            cm -= 1
print(tot**2)
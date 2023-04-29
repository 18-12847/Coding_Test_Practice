import sys
n, k = map(int, sys.stdin.readline().split())
lst = [[0,0] for _ in range(6)]
for i in range(n):
    s, y = map(int, sys.stdin.readline().split())
    if s:
        lst[y-1][1] += 1
    else:
        lst[y-1][0] += 1
tot = 0
for i in lst:
    tot += (i[0] // k + (1 if i[0] % k else 0)) + (i[1] // k + (1 if i[1] % k else 0))
print(tot)
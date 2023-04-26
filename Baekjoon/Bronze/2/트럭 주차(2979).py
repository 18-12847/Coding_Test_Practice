import sys
a, b, c = map(int, sys.stdin.readline().split())
ans = []
for i in range(3):
    x, y = map(int, sys.stdin.readline().split())
    for j in range(x, y):
        ans.append(j)
ans.sort()
tot = 0
for i in ans:
    if ans.count(i) == 1:
        tot += a
    elif ans.count(i) == 2:
        tot += b
    else:
        tot += c
print(tot)
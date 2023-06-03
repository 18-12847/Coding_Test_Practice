import sys
n, m = map(int, sys.stdin.readline().split())
lst = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(n)], key = lambda x: (x[1], x[2], x[3]), reverse = True)
cnt = 1
lst[0].append(1)
for i in range(1, n):
    if lst[i][1:4] != lst[i-1][1:4]:
        cnt = i + 1
    lst[i].append(cnt)
for i in lst:
    if i[0] == m:
        print(i[-1])
        break
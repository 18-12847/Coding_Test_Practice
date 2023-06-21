import sys
n, m = map(int, sys.stdin.readline().split())
flag = [[False] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    flag[a][b] = flag[b][a] = True
cnt = 0
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if flag[i][j]:
            continue
        for k in range(j + 1, n + 1):
            if not(flag[i][k] or flag[j][k]):
                cnt += 1
print(cnt)
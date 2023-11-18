import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
dp = [[1] * m] + [[0] * m for _ in range(n - 1)]
for i in range(n):
    dp[i][0] = 1
cnt = 0
if k:
    for i in range(n):
        for j in range(m):
            cnt += 1
            if cnt == k:
                x, y = j, i
                break
    for i in range(y + 1):
        for j in range(x + 1):
            if not dp[i][j]:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    for i in range(x, m):
        dp[y][i] = dp[y][x]
    for j in range(y, n):
        dp[j][x] = dp[y][x]
    for i in range(y + 1, n):
        for j in range(x + 1, m):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    print(dp[-1][-1])
else:
    for y in range(1, n):
        for x in range(1, m):
            dp[y][x] = dp[y][x - 1] + dp[y - 1][x]
    print(dp[-1][-1])
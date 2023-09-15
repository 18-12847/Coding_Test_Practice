import sys
input = sys.stdin.readline
n = int(input().rstrip())
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 1)
for i in range(n-1, -1, -1):
    if lst[i][0] + i > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(lst[i][1] + dp[lst[i][0] + i], dp[i+1])
print(dp[0])
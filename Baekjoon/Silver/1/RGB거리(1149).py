import sys
input = sys.stdin.readline
n = int(input().rstrip())
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [[0, 0, 0] for _ in range(n)]
dp[0] = lst[0]
for i in range(1, n):
    dp[i][0] = min(dp[i-1][1] + lst[i][0], dp[i-1][2] + lst[i][0])
    dp[i][1] = min(dp[i-1][0] + lst[i][1], dp[i-1][2] + lst[i][1])
    dp[i][2] = min(dp[i-1][0] + lst[i][2], dp[i-1][1] + lst[i][2])
print(min(dp[-1]))
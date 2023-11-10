import sys
input = sys.stdin.readline
n = int(input().rstrip())
lst = [int(input().rstrip()) for _ in range(n)]
dp = [0] * 10000
dp[0] = lst[0]
if n > 2:
    dp[1] = dp[0] + lst[1]
    dp[2] = max(dp[1], dp[0] + lst[2], lst[1] + lst[2])
    for i in range(3, n):
        dp[i] = max(dp[i - 1], dp[i - 3] + lst[i - 1] + lst[i], dp[i - 2] + lst[i])
else:
    dp[n - 1] = sum(lst)
print(dp[n - 1])
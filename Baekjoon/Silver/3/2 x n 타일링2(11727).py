import sys
input = sys.stdin.readline
n = int(input().rstrip())
dp = [0, 1, 3] + [0] * (n - 2)
for i in range(3, n+1):
    dp[i] = (dp[i-2] * 2 + dp[i-1]) % 10007
print(dp[n])
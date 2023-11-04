import sys
input = sys.stdin.readline
n = int(input().rstrip())
dp = [0, 3, 7, 17, 41] + [0] * (n - 4)
for i in range(5, n + 1):
    dp[i] = (dp[i - 1] * 2 + dp[i - 2]) % 9901
print(dp[n])
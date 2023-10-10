import sys
input = sys.stdin.readline
dp = [0, 1, 2, 4] + [0] * (999997)
for i in range(4, 1000001):
    dp[i] = (dp[i - 3] + dp[i - 2] + dp[i - 1]) % 1000000009
for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    print(dp[n])
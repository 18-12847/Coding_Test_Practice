import sys
input = sys.stdin.readline
n = int(input().rstrip())
dp = [0, 0, 1, 0, 0] + [1] * (n - 4)
for i in range(5, n + 1):
    if dp[i-1] or dp[i-3] or dp[i-4]:
        dp[i] = 0
print("CY" if dp[n] else "SK")
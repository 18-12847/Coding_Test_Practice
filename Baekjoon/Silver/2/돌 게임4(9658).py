import sys
input = sys.stdin.readline
n = int(input().rstrip())
dp = [0, 1, 0, 1, 0] + [0] * 996
for i in range(5, n + 1):
    if not dp[i - 1] and not dp[i - 3] and not dp[i - 4]:
        dp[i] = 1
    else:
        dp[i] = 0
print("CY" if dp[n] else "SK")
import sys
input = sys.stdin.readline
n = int(input().rstrip())
dp = [0] * 36
dp[0] = 1
for i in range(1, 36):
    for j in range(i-1, -1, -1):
        dp[i] += dp[i-j-1] * dp[j]
print(dp[n])
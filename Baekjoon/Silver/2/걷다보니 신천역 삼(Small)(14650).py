import sys
input = sys.stdin.readline
n = int(input().rstrip())
dp = [0, 2, 6]  + [0] * 6
for i in range(3, 9):
    dp[i] = dp[i -1] * 3
print(dp[n-1])
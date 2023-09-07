import sys
input = sys.stdin.readline
for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    dp = [0] * 11
    dp[0], dp[1], dp[2] = 1, 2, 4
    for i in range(3, n):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n-1])
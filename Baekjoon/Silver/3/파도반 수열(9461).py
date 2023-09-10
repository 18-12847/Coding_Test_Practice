import sys
input = sys.stdin.readline
for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    dp = [1, 1, 1, 2, 2] + [0] * (n - 5)
    for i in range(5, n):
        dp[i] = dp[i-5] + dp[i-1]
    print(dp[n-1])

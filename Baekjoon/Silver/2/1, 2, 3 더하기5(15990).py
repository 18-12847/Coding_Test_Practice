import sys
input = sys.stdin.readline
mx, mod = 100001, 1000000009
dp = [[0, 0, 0] for _ in range(mx)]
dp[1], dp[2], dp[3] = [1, 0, 0], [0, 1, 0], [1, 1, 1]
for i in range(4, mx):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % mod
    dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % mod
    dp[i][2] = (dp[i-3][1] + dp[i-3][0]) % mod
for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    print(sum(dp[n]) % mod)
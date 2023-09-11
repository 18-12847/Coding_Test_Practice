import sys
input = sys.stdin.readline
n = int(input().rstrip())
if n < 0:
    dp = [1, 0] + [0] * abs(n)
    for i in range(2, abs(n) + 2):
        if dp[i-2] - dp[i-1] > 0:
            dp[i] = (dp[i-2] - dp[i-1]) % 1000000000
        else:
            dp[i] = (dp[i-2] - dp[i-1]) % -1000000000
    if dp[-1] < 0:
        print(-1, abs(dp[-1]), sep = "\n")
    else:
        print(1, dp[-1], sep = "\n")
elif n == 0:
    print(0, 0, sep = "\n")
else:
    dp = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        dp[i] = (dp[i-2] + dp[i-1]) % 1000000000
    print(1, dp[-1], sep = "\n")
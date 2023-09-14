import sys
input = sys.stdin.readline
n = int(input().rstrip())
lst = [int(input().rstrip()) for _ in range(n)]
if n < 3:
    print(sum(lst))
else:
    dp = [0] * n
    dp[0], dp[1] = lst[0], lst[0] + lst[1]
    dp[2] = max(lst[0] + lst[2], lst[1] + lst[2])
    for i in range(3, n):
        dp[i] = max(dp[i-3] + lst[i-1] + lst[i], dp[i-2] + lst[i])
    print(dp[n-1])
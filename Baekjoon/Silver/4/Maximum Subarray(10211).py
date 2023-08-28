import sys
input = sys.stdin.readline
for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    lst = list(map(int, input().split()))
    dp = [0] * n
    tot, dp[0] = 0, lst[0]
    for i in range(1, n):
        if dp[i-1] + lst[i] > lst[i]:
            dp[i] = dp[i-1] + lst[i]
        else:
            dp[i] = lst[i]
    print(max(dp))
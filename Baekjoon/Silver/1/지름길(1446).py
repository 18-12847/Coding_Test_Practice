import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dp = [i for i in range(m + 1)]
lst = [list(map(int, input().split())) for _ in range(n)]
for i in range(m + 1):
    dp[i] = min(dp[i], dp[i - 1] + 1)
    for start, end, dist in lst:
        if i == start and end <= m:
            dp[end] = min(dp[end], dp[start] + dist)
print(dp[-1])
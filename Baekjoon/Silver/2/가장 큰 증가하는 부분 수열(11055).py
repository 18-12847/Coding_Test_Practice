import sys
input = sys.stdin.readline
n = int(input().rstrip())
lst = list(map(int, input().split()))
dp = lst.copy()
for i in range(1, n):
    for j in range(i):
        if lst[i] > lst[j] and dp[i] < dp[j] + lst[i]:
            dp[i] = dp[j] + lst[i]
print(max(dp))
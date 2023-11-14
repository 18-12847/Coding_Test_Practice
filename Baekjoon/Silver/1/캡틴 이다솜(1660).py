import sys
input = sys.stdin.readline
n = int(input().rstrip())
ball = [1] + [0] * 119
for i in range(1, 120):
    ball[i] = ball[i - 1] + i + 1
for i in range(1, 120):
    ball[i] += ball[i - 1]
dp = [0] * 300001
for i in ball:
    dp[i] = 1
for i in range(2, n + 1):
    if dp[i] != 0:
        continue
    dp[i] = min(dp[i-j] for j in ball if j < i) + 1
print(dp[n])
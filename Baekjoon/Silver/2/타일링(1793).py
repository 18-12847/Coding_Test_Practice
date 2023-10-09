import sys
input = sys.stdin.readline
dp = [1, 1, 3] + [0] * 248
for i in range(3, 251):
    dp[i] = dp[i - 1] + 2 * dp[i - 2]
while True:
    try:
        n = int(input().rstrip())
        print(dp[n])
    except:
        exit()
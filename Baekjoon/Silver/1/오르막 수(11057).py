import sys
input = sys.stdin.readline
dp = [0, 10, 55] + [0] * 998
lst = [i for i in range(10, 0, -1)]
for i in range(3, 1001):
    tmp = [dp[i - 1]] + [0] * 9
    for j in range(1, 10):
        tmp[j] = tmp[j - 1] - lst[j - 1]
    dp[i], lst = sum(tmp), tmp
print(dp[int(input().rstrip())] % 10007)
import sys
input = sys.stdin.readline
n = int(input().rstrip())
lst = [float(input().rstrip()) for _ in range(n)]
dp = [0.0] * n
for i in range(n):
    tot, maxx = 1, 0
    for j in range(i, n):
        tot *= lst[j]
        if tot > maxx:
            maxx = tot
    dp[i] = maxx
print(f"{max(dp):.3f}")
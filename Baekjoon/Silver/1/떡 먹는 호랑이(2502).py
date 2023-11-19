import sys
input = sys.stdin.readline
def solve():
    n, m = map(int, input().split())
    for i in range(1, m + 1):
        for j in range(1, m + 1):
            dp = [i, i + j]
            for _ in range(n - 2):
                if dp[-1] + dp[-2] > m:
                    break
                dp.append(dp[-1] + dp[-2])
            if len(dp) == n and dp[-1] == m:
                print(dp[0])
                print(dp[1])
                return

solve()
import sys
input = sys.stdin.readline
n = int(input().rstrip())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
for y in range(n):
    for x in range(n):
        if graph[y][x] != 0 and dp[y][x] != 0:
            if y + graph[y][x] < n:
                dp[y + graph[y][x]][x] += dp[y][x]
            if x + graph[y][x] < n:
                dp[y][x + graph[y][x]] += dp[y][x]
print(dp[-1][-1])
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(x, y):
    cnt.append(1)
    graph[y][x] = "."
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == "#":
            dfs(nx, ny)

n, m, k = map(int, input().split())
graph = [["." for _ in range(m)] for _ in range(n)]
for _ in range(k):
    y, x = map(int, input().split())
    graph[y-1][x-1] = "#"
ans = []
for y in range(n):
    for x in range(m):
        if graph[y][x] == "#":
            cnt = []
            dfs(x, y)
            ans.append(len(cnt))
print(max(ans))
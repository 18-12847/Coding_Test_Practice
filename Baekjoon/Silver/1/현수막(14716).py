import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(x, y):
    graph[y][x] = 0
    dx = [0, 0, -1, 1, -1, 1, 1, -1]
    dy = [-1, 1, 0, 0, -1, -1, 1, 1]
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[ny][nx]:
            dfs(nx, ny)

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
cnt = 0
for y in range(m):
    for x in range(n):
        if graph[y][x]:
            dfs(x, y)
            cnt += 1
print(cnt)
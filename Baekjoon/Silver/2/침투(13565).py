import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(x, y):
    graph[y][x] = "2"
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[ny][nx] == "0":
            dfs(nx, ny)

m, n = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(m)]
for x in range(n):
    if graph[0][x] == "0":
        dfs(x, 0)
if "2" in graph[0] and "2" in graph[-1]:
    print("YES")
else:
    print("NO")
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

dirs = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, -1), (1, 1), (-1, 1)]
def dfs(y, x):
    check = 1
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n:
            if graph[y][x] < graph[ny][nx]:
                check = 0
            if not visited[ny][nx] and graph[y][x] == graph[ny][nx]:
                visited[ny][nx] = 1
                if not dfs(ny, nx):
                    check = 0
    return check
    
n, m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            cnt += dfs(i, j)
print(cnt)
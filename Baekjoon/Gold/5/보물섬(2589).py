import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(cy, cx):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[cy][cx] = 1
    queue = deque([(cy, cx, 0)])
    while queue:
        y, x, depth = queue.popleft()
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and graph[ny][nx] == "L":
                queue.append((ny, nx, depth + 1))
                visited[ny][nx] = visited[y][x] + 1
    return depth

mx = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == "L":
            mx = max(mx, bfs(i, j))
print(mx)
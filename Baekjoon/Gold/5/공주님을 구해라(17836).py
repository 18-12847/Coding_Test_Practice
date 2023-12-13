import sys
input = sys.stdin.readline
from collections import deque

dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
def bfs():
    global gram
    while queue:
        y, x, depth = queue.popleft()
        if graph[y][x] == 2:
            gram = depth + (n - y - 1) + (m - x - 1)
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
                if graph[ny][nx] == 1:
                    continue
                visited[ny][nx] = visited[y][x] + 1
                queue.append((ny, nx, depth + 1))

n, m, t = map(int, input().split())
queue = deque([(0, 0, 0)])
visited = [[0] * m for _ in range(n)]
gram = 12345
graph = [list(map(int, input().split())) for _ in range(n)]

bfs()
ans = min(visited[-1][-1], gram)
if not visited[-1][-1]:
    print("Fail" if gram > t else gram)
else:
    print("Fail" if ans > t else ans)
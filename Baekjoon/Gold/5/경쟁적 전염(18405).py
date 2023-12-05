import sys
input = sys.stdin.readline
from collections import deque

dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
def bfs():
    while queue:
        cy, cx, second = queue.popleft()
        if second == s:
            return
        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
                visited[ny][nx] = visited[cy][cx]
                queue.append((ny, nx, second + 1))

queue = deque([])
n, k = map(int, input().split())
graph = []
visited = [[0] * n for _ in range(n)]
tmp = []
for i in range(n):
    inp = list(map(int, input().split()))
    for j in range(n):
        visited[i][j] = inp[j]
        if inp[j]:
            tmp.append((inp[j], i, j, 0))
    graph.append(inp)
for i in sorted(tmp):
    queue.append(i[1:])
s, x, y = map(int, input().split())

bfs()
print(visited[x - 1][y - 1])
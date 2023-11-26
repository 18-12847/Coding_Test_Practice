import sys
input = sys.stdin.readline
from collections import deque

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs():
    while queue:
        y, x, depth = queue.popleft()
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < col and 0 <= ny < row and not visited[ny][nx]:
                if graph[ny][nx] == -1:
                    continue
                if not graph[ny][nx]:
                    queue.append((ny, nx, depth + 1))
                    visited[ny][nx] = visited[y][x] + 1
    return depth

col, row = map(int, input().split())
visited = [[0] * col for _ in range(row)]
queue = deque()
graph = []
for i in range(row):
    lst = list(map(int, input().split()))
    for j in range(col):
        if lst[j] == 1:
            queue.append((i, j, 0))
            visited[i][j] = 1
    graph.append(lst)

if queue:
    ans = bfs()
else:
    print(-1)
    exit()
    
cnt1, cnt2 = 0, 0
for i in range(row):
    cnt1 += visited[i].count(0)
    cnt2 += graph[i].count(-1)
print(ans if cnt1 == cnt2 else -1)
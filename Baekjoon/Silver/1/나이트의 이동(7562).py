import sys
input = sys.stdin.readline
from collections import deque

dirs = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
def bfs():
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[y1][x1] = 0
    queue = deque([[y1, x1]])
    while queue:
        y, x = queue.popleft()
        if [y, x] == [y2, x2]:
            print(visited[y][x])
            break
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == -1:
                queue.append([ny, nx])
                visited[ny][nx] = visited[y][x] + 1

for i in range(int(input().rstrip())):
    n = int(input().rstrip())
    y1, x1 = map(int, input().split())
    y2, x2 = map(int, input().split())
    bfs()
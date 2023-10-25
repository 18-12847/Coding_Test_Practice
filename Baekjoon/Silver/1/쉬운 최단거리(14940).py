import sys
input = sys.stdin.readline
from collections import deque

dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
def bfs():
    queue = deque([[gy, gx]])
    while queue:
        y, x = queue.popleft()
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == -1: #범위 안에서 방문 안했고
                if graph[ny][nx]: #해당 위치가 1이면
                    queue.append([ny, nx]) #추가 후
                    visited[ny][nx] = visited[y][x] + 1 #방문 표시
                elif not graph[ny][nx]: #벽이면
                    visited[ny][nx] = 0 #0으로 표시    
    for i in visited:
        print(*i)

n, m = map(int, input().split())
graph = []
visited = [[-1 for _ in range(m)] for _ in range(n)]
for i in range(n):
    lst = list(map(int, input().split()))
    if 2 in lst:
        gy, gx = i, lst.index(2) #시작점 찾기
    for j in range(m):
        if not lst[j]:
            visited[i][j] = 0 #벽 표시
    graph.append(lst)
visited[gy][gx] = 0

bfs()
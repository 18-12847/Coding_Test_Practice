import sys
input = sys.stdin.readline
from collections import deque

dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
def bfs():
    queue = deque([(0, 0)])
    while queue:
        y, x = queue.popleft()
        if (y, x) == (n - 1, m - 1):
            print(visited[n-1][m-1])
            exit()
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] and not visited[ny][nx]:
                queue.append([ny, nx])
                visited[ny][nx] = visited[y][x] + 1

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for i in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
visited[0][0] = 1 #visited꼭 적용하자!!!!!

bfs()
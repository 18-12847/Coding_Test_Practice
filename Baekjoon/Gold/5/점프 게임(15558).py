import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    visited = [[0] * n for _ in range(2)]
    queue = deque([(0, 0, 0)])
    while queue:
        y, x, time = queue.popleft()
        for loc in (1, -1, k):
            nx = x + loc
            if nx >= n:
                print(1)
                exit()
            if time < nx and graph[y][nx] and loc != k and not visited[y][nx]:
                visited[y][nx] = 1
                queue.append((y, nx, time + 1))
            elif time < nx and graph[1 - y][nx] and loc == k and not visited[1 - y][nx]:
                visited[1 - y][nx] = 1
                queue.append((1 - y, nx, time + 1))

n, k = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for _ in range(2)]
bfs()
print(0)
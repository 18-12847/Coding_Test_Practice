import sys
input = sys.stdin.readline
from collections import deque

def bfs(start, end):
    queue = deque([(start, 0)])
    visited = [0] * (n + 1)
    visited[start] = 1
    while queue:
        cur, dist = queue.popleft()
        if cur == end:
            return dist
        for i, d in graph[cur]:
            if not visited[i]:
                visited[i] = 1
                queue.append((i, d + dist))

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y, distance = map(int, input().split())
    graph[x].append((y, distance))
    graph[y].append((x, distance))

for _ in range(m):
    a, b = map(int, input().split())
    print(bfs(a, b))
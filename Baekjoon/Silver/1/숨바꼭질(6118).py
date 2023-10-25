import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    queue = deque([1])
    visited = [-1] * (n + 1)
    visited[1] = 0
    while queue:
        cur = queue.popleft()
        for i in graph[cur]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[cur] + 1
    return visited

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]
for i in range(1, n + 1):
    graph[i] = sorted(graph[i])

visited = bfs()
mx = max(visited)
print(visited.index(mx), mx, visited.count(mx))
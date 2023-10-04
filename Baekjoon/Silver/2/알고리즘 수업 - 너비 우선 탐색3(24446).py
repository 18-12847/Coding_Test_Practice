import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    queue = deque([start])
    visited[start] = 0
    while queue:
        cur = queue.popleft()
        for i in graph[cur]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[cur] + 1 #현재 노드의 깊이에 1을 더하면 자식 노드

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u] += [v]
    graph[v] += [u]

visited = [-1] * (n + 1)
bfs(r)
print(*visited[1:], sep = "\n")
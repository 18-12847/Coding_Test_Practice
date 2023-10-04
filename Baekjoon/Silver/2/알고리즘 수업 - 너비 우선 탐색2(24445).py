import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    queue = deque([start])
    cnt = 1
    visited[start] = cnt
    while queue:
        cur = queue.popleft()
        for i in graph[cur]:
            if not visited[i]:
                cnt += 1
                queue.append(i)
                visited[i] = cnt #방문 정점 표시를 순서로 해준다

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u] += [v]
    graph[v] += [u]
for i in range(1, n + 1):
    graph[i] = sorted(graph[i])[::-1]

visited = [0] * (n + 1)
bfs(r)
print(*visited[1:], sep = "\n")
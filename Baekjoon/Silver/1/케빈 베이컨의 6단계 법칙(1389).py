import sys
input = sys.stdin.readline
from collections import deque

def bfs(node):
    visited = [0] * (n + 1)
    visited[node] = 0
    queue = deque([node])
    while queue:
        cur = queue.popleft()
        for x in graph[cur]:
            if not visited[x]:
                queue.append(x)
                visited[x] = visited[cur] + 1
    return sum(visited) - 2

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]
for i in range(1, n + 1):
    graph[i] = sorted(graph[i])

ans = [0] * (n + 1)
for i in range(1, n + 1):
    ans[i] = bfs(i)
print(ans.index(min(ans[1:])))
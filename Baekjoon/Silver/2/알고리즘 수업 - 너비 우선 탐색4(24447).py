import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    cnt = 1
    ans[start], visited[start] = cnt, cnt
    queue = deque([start])
    while queue:
        cur = queue.popleft()
        ans[cur] = cnt
        for i in graph[cur]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[cur] + 1
        cnt += 1

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
ans = [0] * (n + 1)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u] += [v]
    graph[v] += [u]
for i in range(1, n + 1):
    graph[i] = sorted(graph[i])

bfs(r)
print(sum(ans[i] * (visited[i] - 1) for i in range(1, n + 1)))
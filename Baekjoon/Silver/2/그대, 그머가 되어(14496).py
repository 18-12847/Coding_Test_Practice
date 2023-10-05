import sys
input = sys.stdin.readline
from collections import deque

a, b = map(int, input().split())
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x] += [y]
    graph[y] += [x]
visited = [0] * (n + 1)
queue = deque([a])

while queue:
    cur = queue.popleft()
    if cur == b:
        print(visited[cur])
        exit()
    for i in graph[cur]:
        if not visited[i]:
            queue.append(i)
            visited[i] = visited[cur] + 1
print(-1)
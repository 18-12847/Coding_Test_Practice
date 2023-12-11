import sys
input = sys.stdin.readline
from collections import deque

def bfs(v):
    visited = [0] * (n + 1)
    queue = deque([(v, 0)])
    visited[v] = 1
    while queue:
        cur, dep = queue.popleft()
        for i in graph[cur]:
            if not visited[i]:
                queue.append((i, dep + 1))
                visited[i] = 1
    return [v, dep]

n = int(input().rstrip())
graph = [[] for _ in range(n + 1)]
while True:
    a, b = map(int, input().split())
    if a == -1:
        break
    graph[a] += [b]
    graph[b] += [a]

ans = [bfs(i)[1] for i in range(1, n + 1)]
mn = min(ans)
print(mn, ans.count(mn))
for i in range(n):
    if ans[i] == mn:
        print(i + 1, end = " ")

# import sys
# input = sys.stdin.readline
# n = int(input().rstrip())
# graph = [[51] * (n + 1) for _ in range(n + 1)]
# for i in range(1, n + 1):
#     graph[i][i] = 0
# while True:
#     a, b = map(int, input().split())
#     if a == -1:
#         break
#     graph[a][b] = 1
#     graph[b][a] = 1
# ans = []
# for k in range(1, n + 1):
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             if graph[i][j] > graph[i][k] + graph[k][j]:
#                 graph[i][j] = graph[i][k] + graph[k][j]
# for i in range(1, n + 1):
#     ans.append(max(graph[i][1:]))
# mn = min(ans)
# print(mn, ans.count(mn))
# for i in range(n):
#     if ans[i] == mn:
#         print(i + 1, end = " ")
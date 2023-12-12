import sys
input = sys.stdin.readline

def dfs(cur, start):
    visited[cur] = 1
    for v in graph[cur]:
        if not visited[v]:
            dfs(v, start)
        elif visited[v] and v == start:
            ans.add(v)

n = int(input().rstrip())
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[int(input().rstrip())] += [i]

ans = set()
for i in range(1, n + 1):
    if graph[i]:
        visited = [0] * (n + 1)
        dfs(i,i)
print(len(ans))
print(*sorted(ans), sep = "\n")

# import sys
# input = sys.stdin.readline
# from collections import deque

# def bfs(v):
#     visited[v] = 1
#     queue = deque([v])
#     while queue:
#         cur = queue.popleft()
#         for i in graph[cur]:
#             if not visited[i]:
#                 queue.append(i)
#             elif visited[i] and i == v:
#                 ans.add(i)

# n = int(input().rstrip())
# graph = [[] for _ in range(n + 1)]
# for i in range(1, n + 1):
#     graph[int(input().rstrip())] += [i]

# ans = set()
# for i in range(1, n + 1):
#     if graph[i]:
#         visited = [0] * (n + 1)
#         bfs(i)
# print(len(ans))
# print(*sorted(ans), sep = "\n")
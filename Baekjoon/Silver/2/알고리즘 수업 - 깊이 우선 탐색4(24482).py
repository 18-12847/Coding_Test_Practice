import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(v, depth):
    if visited[v] != -1:
        return
    visited[v] = depth
    for i in graph[v]:
        if visited[i] == -1:
            dfs(i, depth + 1)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x] += [y]
    graph[y] += [x]
for i in range(1, n + 1):
    graph[i] = sorted(graph[i])[::-1]
dfs(r, 0)
print(*visited[1:], sep = "\n")
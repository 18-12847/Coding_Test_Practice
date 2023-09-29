import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u] += [v]
    graph[v] += [u]
cnt = 0
visited = [0] * (n + 1)
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)
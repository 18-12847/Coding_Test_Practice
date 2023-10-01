import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(v):
    global cnt
    visited[v] = cnt
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(i)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 1
for _ in range(m):
    x, y = map(int, input().split())
    graph[x] += [y]
    graph[y] += [x]
for i in range(1, n + 1):
    graph[i] = sorted(graph[i])
dfs(r)
print(*visited[1:], sep = "\n")
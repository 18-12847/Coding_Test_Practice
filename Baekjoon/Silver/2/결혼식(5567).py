import sys
input = sys.stdin.readline

def dfs(v, depth):
    visited[v] = 1
    if depth == 2:
        return
    for i in graph[v]:
        dfs(i, depth + 1)

n = int(input().rstrip())
graph = [[] for _ in range(n + 1)]
for _ in range(int(input().rstrip())):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]
visited = [0] * (n + 1)
dfs(1, 0)
print(sum(visited) - 1)
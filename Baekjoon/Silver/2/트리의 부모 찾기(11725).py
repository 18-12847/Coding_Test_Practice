import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(v):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = v
            dfs(i)

n = int(input().rstrip())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x] += [y]
    graph[y] += [x]
visited = [0] * (n + 1)
dfs(1)
print(*visited[2:], sep = "\n")
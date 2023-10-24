import sys
input = sys.stdin.readline
sys.setrecursionlimit(500000)

def dfs(x, depth):
    global tot
    visited[x] = 1
    if len(graph[x]) == 1:
        tot += depth
    else:
        for idx in graph[x]:
            if not visited[idx]:
                dfs(idx, depth + 1)

n = int(input().rstrip())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0, 1] + [0] * (n - 1)

tot = 0
for i in graph[1]:
    dfs(i, 1)
print("Yes" if tot % 2 else "No")
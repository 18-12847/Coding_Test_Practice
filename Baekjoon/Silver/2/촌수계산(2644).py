import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(x, cnt):
    if x == b:
        print(cnt)
        exit()
    visited[x] = 1
    for i in graph[x]:
        if not visited[i]:
            dfs(i, cnt + 1)
            
n = int(input().rstrip())
a, b = map(int, input().split())
m = int(input().rstrip())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
result = []
for i in range(m):
    x, y = map(int, input().split())
    graph[x] += [y]
    graph[y] += [x]
dfs(a, 0)
print(-1)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(x, y, val):
    visited[y][x] = 1
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] > val and not visited[ny][nx]:
            dfs(nx, ny, val)
    
n = int(input().rstrip())
graph = []
small, big = 101, -1
for _ in range(n):
    lst = list(map(int, input().split()))
    if min(lst) < small:
        small = min(lst)
    if max(lst) > big:
        big = max(lst)
    graph.append(lst)
ans = [0] * (big + 1)

for i in range(small, big + 1):
    visited = [[0] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if graph[y][x] > i and not visited[y][x]:
                dfs(x, y, i)
                ans[i] += 1
print(max(ans) if max(ans) else 1)
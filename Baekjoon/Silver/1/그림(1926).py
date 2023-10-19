import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(x, y):
    tot.append(1)
    graph[y][x] = 0
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[ny][nx]:
            dfs(nx, ny)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cnt, ans = 0, []
for y in range(n):
    for x in range(m):
        if graph[y][x]:
            tot = []
            dfs(x, y)
            ans.append(len(tot))
            cnt += 1
print(cnt)
print(max(ans) if ans else 0)
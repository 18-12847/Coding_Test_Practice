import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(x, y):
    count.append(1)
    graph[y][x] = 0
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[ny][nx]:
                dfs(nx, ny)

n = int(input().rstrip())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
depth, ans = 0, []
for y in range(n):
    for x in range(n):
        if graph[y][x]:
            count = []
            dfs(x, y)
            depth += 1
            ans.append(len(count))
print(depth)
print(*sorted(ans), sep = "\n")
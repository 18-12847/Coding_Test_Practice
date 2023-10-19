import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(x, y):
    graph[y][x] = 1
    count.append(1)
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < cols and 0 <= ny < rows:
            if not graph[ny][nx]:
                dfs(nx, ny)

rows, cols, k = map(int, input().split())
graph = [[0 for _ in range(cols)] for _ in range(rows)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for row in range(y1, y2):
        for col in range(x1, x2):
            graph[rows - row - 1][col] = 1
depth, ans = 0, []
for y in range(rows):
    for x in range(cols):
        if not graph[y][x]:
            count = []
            dfs(x, y)
            depth += 1
            ans.append(len(count))
print(depth)
print(*sorted(ans))
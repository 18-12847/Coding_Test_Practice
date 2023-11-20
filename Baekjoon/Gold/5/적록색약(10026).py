import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def dfs(x, y, color):
    visited[y][x] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
            if graph[ny][nx] == color:
                dfs(nx, ny, color)

def check(x, y, color, count):
    if graph[y][x] == color and not visited[y][x]:
        dfs(x, y, color)
        count += 1
    return count

n = int(input().rstrip())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

cnt1, cnt2 = 0, 0
for y in range(n):
    for x in range(n):
        cnt1 = check(x, y, "R", cnt1)
        cnt1 = check(x, y, "G", cnt1)
        cnt1 = check(x, y, "B", cnt1)

visited = [[0 for _ in range(n)] for _ in range(n)]
for y in range(n):
    for x in range(n):
        if graph[y][x] == "G":
            graph[y][x] = "R"
            
for y in range(n):
    for x in range(n):
        cnt2 = check(x, y, "R", cnt2)
        cnt2 = check(x, y, "B", cnt2)
print(cnt1, cnt2)
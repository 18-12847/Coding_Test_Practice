import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(x, y):
    graph[y][x] = "."
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < w and 0 <= ny < h and graph[ny][nx] == "#":
            dfs(nx, ny)

for _ in range(int(input().rstrip())):
    h, w = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(h)]
    cnt = 0
    for y in range(h):
        for x in range(w):
            if graph[y][x] == "#":
                dfs(x, y)
                cnt += 1
    print(cnt)
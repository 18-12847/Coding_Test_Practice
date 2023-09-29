import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x, y):
    if graph[y][x] == 1:
        graph[y][x] = 0
    dx = [0, 0, -1, 1, -1, 1, 1, -1]
    dy = [1, -1, 0, 0, 1, 1, -1, -1]
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < a and 0 <= ny < b:
            if graph[ny][nx] == 1:
                dfs(nx, ny)

while True:
    a, b = map(int, input().split())
    if [a, b] == [0, 0]:
        exit()
    graph = [list(map(int, input().split())) for _ in range(b)]
    cnt = 0
    for y in range(b):
        for x in range(a):
            if graph[y][x] == 1:
                dfs(x, y)
                cnt += 1
    print(cnt)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(x, y, arr, tlqkf):
    arr.append(1)
    graph[y][x] = "X"
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[ny][nx] == tlqkf:
            dfs(nx, ny, arr, tlqkf)

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(m)]
ans = [0, 0]
for y in range(m):
    for x in range(n):
        if graph[y][x] == "W":
            w_cnt = []
            dfs(x, y, w_cnt, "W")
            ans[0] += len(w_cnt) ** 2
        elif graph[y][x] == "B":
            b_cnt = []
            dfs(x, y, b_cnt, "B")
            ans[1] += len(b_cnt) ** 2
print(*ans)
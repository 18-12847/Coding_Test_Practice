import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(x, y):
    if graph[y][x] == "k":
        cnt[0] += 1
    elif graph[y][x] == "v":
        cnt[1] += 1
    graph[y][x] = "X"
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < c and 0 <= ny < r and graph[ny][nx] not in "X#":
            dfs(nx, ny)

r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
ans = [0, 0]
for y in range(r):
    for x in range(c):
        if graph[y][x] in "kv":
            cnt = [0, 0]
            dfs(x, y)
            if cnt[0] > cnt[1]:
                ans[0] += cnt[0]
            else:
                ans[1] += cnt[1]
print(*ans)
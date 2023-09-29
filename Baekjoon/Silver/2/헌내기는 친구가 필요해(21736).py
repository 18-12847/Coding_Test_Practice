#BFS로 다시 풀어야하는 문제
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(y, x):
    global cnt
    if graph[y][x] == "P":
        cnt += 1
    graph[y][x] = "V"
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if graph[ny][nx] != "X" and graph[ny][nx] != "V":
                dfs(ny, nx)

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == "I":
            dfs(i, j)
print(cnt if cnt else "TT")
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(x, y, s):
    if len(s) == 6:
        answer.add(s)
        return
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, s + graph[ny][nx])

graph = [list(input().split()) for _ in range(5)]
answer = set()
for y in range(5):
    for x in range(5):
        s = ""
        dfs(x, y, s + graph[y][x])
print(len(answer))
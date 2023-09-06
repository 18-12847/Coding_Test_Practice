import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(x, y):
    if [x, y] == [n-1, n-1]:
        print("HaruHaru")
        exit()
    if graph[y][x] == 0:
        return
    if x + graph[y][x] <= n - 1:
        dfs(x + graph[y][x], y)
    if y + graph[y][x] <= n - 1:
        dfs(x, y + graph[y][x])

n = int(input().rstrip())
graph = [list(map(int, input().split())) for _ in range(n)]
dfs(0, 0)
print("Hing")
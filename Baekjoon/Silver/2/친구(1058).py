import sys
input = sys.stdin.readline
n = int(input().rstrip())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if graph[i][j] == "Y" or (graph[i][k] == "Y" and graph[k][j] == "Y"):
                visited[i][j] = 1
print(max(map(sum, visited)))
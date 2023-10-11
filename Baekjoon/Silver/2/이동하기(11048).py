import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, n):
    graph[i][0] += graph[i-1][0]
for j in range(1, m):
    graph[0][j] += graph[0][j-1]
for i in range(1, n):
    for j in range(1, m):
        graph[i][j] += max(graph[i-1][j], graph[i][j-1])
print(graph[-1][-1])
import sys, heapq
input = sys.stdin.readline

def floyd():
    n, m = map(int, input().split())
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1
    cnt = 0
    for i in range(1, n + 1):
        heavy = sum(graph[i])
        light = sum(row[i] for row in graph)
        if heavy > n // 2 or light > n // 2:
            cnt += 1
    print(cnt)

floyd()
import sys, heapq
input = sys.stdin.readline

def floyd():
    n = int(input().rstrip())
    m = int(input().rstrip())
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            if not graph[i][k]:
                continue
            for j in range(1, n + 1):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1
    total = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j]:
                total[i] += 1
                total[j] += 1
    for i in total[1:]:
        print(n - i - 1)

floyd()
import sys
input = sys.stdin.readline
inf = 999999999

def floyd():
    n = int(input().rstrip())
    m = int(input().rstrip())
    visited = [[inf] * (n + 1) for _ in range(n + 1)]
    for i in range(m):
        a, b, c = map(int, input().split())
        if visited[a][b] > c:
            visited[a][b] = c
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    visited[i][j] = 0
                if visited[i][j] > visited[i][k] + visited[k][j]:
                    visited[i][j] = visited[i][k] + visited[k][j]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if visited[i][j] == inf:
                print(0, end = " ")
            else:
                print(visited[i][j], end = " ")
        print()

floyd()
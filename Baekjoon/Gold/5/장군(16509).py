import sys
input = sys.stdin.readline
from collections import deque

dirs = [(-2, -3), (-2, 3), (-3, -2), (-3, 2), (2, -3), (2, 3), (3, -2), (3, 2)]
check = [[(0, -1), (-1, -2)], [(0, 1), (-1, 2)],
         [(-1, 0), (-2, -1)], [(-1, 0), (-2, 1)],
         [(0, -1), (1, -2)], [(0, 1), (1, 2)],
         [(1, 0), (2, -1)], [(1, 0), (2, 1)]]
def bfs(graph, sy, sx, ey, ex):
    queue = deque([(sy, sx)])
    while queue:
        cy, cx = queue.popleft()
        if (cy, cx) == (ey, ex):
            return graph[cy][cx] - 1
        for idx, (dx, dy) in enumerate(dirs):
            nx = cx + dx
            ny = cy + dy
            if not(0 <= nx < 9 and 0 <= ny < 10) or graph[ny][nx]:
                continue
            flag = False
            for x, y in check[idx]:
                if (cy + y, cx + x) == (ey, ex):
                    flag = True
                    break
            if flag:
                continue
            graph[ny][nx] = graph[cy][cx] + 1
            queue.append((ny, nx))
    return -1

def solve():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    graph = [[0] * 9 for _ in range(10)]
    graph[r1][c1] = 1
    print(bfs(graph, r1, c1, r2, c2))

solve()

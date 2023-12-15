import sys
input = sys.stdin.readline
from collections import deque

dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
def bfs():
    while queue:
        cnt, cy, cx = queue.popleft()
        for dx, dy in dirs:
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < col and 0 <= ny < row and graph[ny][nx] in [".", "D"]:
                if graph[cy][cx] == "*":
                    if graph[ny][nx] == "D":
                        continue
                    graph[ny][nx] = "*"
                    queue.append((0, ny, nx))
                elif graph[cy][cx] == "X":
                    continue
                else:
                    if graph[ny][nx] == "D":
                        return print(cnt + 1)
                    graph[ny][nx] = cnt + 1
                    queue.append((cnt + 1, ny, nx))
    return print("KAKTUS")

row, col = map(int, input().split())
graph = []
queue = deque([])
for i in range(row):
    lst = list(input().rstrip())
    for j in range(col):
        if lst[j] == "*":
            queue.append((0, i, j))
        if lst[j] == "S":
            tmp = (0, i, j)
    graph.append(lst)
queue.append(tmp)
bfs()
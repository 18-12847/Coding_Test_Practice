import sys
input = sys.stdin.readline
from collections import deque

dirs = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
def bfs():
    while queue:
        z, y, x, dep = queue.popleft()
        for dz, dy, dx in dirs:
            nz, ny, nx = z + dz, y + dy, x + dx
            if 0 <= nx < width and 0 <= ny < height and 0 <= nz < depth and not visited[nz][ny][nx]:
                if graph[nz][ny][nx] == "#":
                    continue
                if graph[nz][ny][nx] == ".":
                    queue.append((nz, ny, nx, dep + 1))
                    visited[nz][ny][nx] = visited[z][y][x] + 1
                if graph[nz][ny][nx] == "E":
                    return print(f"Escaped in {dep + 1} minute(s).")
    print("Trapped!")

while True:
    depth, height, width = map(int, input().split())
    if (depth, height, width) == (0, 0, 0):
        exit()
    graph = [[[] for _ in range(height)] for _ in range(depth)]
    visited = [[[0 for _ in range(width)] for _ in range(height)] for _ in range(depth)]
    queue = deque([])
    for i in range(depth):
        for j in range(height + 1):
            inp = list(input().rstrip())
            if "S" in inp:
                k = inp.index("S")
                queue.append((i, j, k, 0))
                visited[i][j][k] = 1
            if inp:
                graph[i][j] = inp
    bfs()
import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    visited = ["use the stairs"] * (tot + 1)
    visited[start] = 0
    queue = deque([start])
    while queue:
        cur = queue.popleft()
        for i in [cur + up, cur - down]:
            if 0 < i <= tot and visited[i] == "use the stairs":
                queue.append(i)
                visited[i] = visited[cur] + 1
    return visited[goal]

tot, start, goal, up, down = map(int, input().split())
print(bfs())
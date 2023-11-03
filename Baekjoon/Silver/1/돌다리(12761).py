import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    visited = [-1] * 100001
    visited[start] = 0
    queue = deque([start])
    while queue:
        cur = queue.popleft()
        if cur == end:
            print(visited[cur])
            exit()
        for i in [cur - 1, cur + 1, cur - power1, cur + power1, cur - power2, cur + power2, cur * power1, cur * power2]:
            if 0 < i < 100001 and visited[i] == -1:
                queue.append(i)
                visited[i] = visited[cur] + 1

power1, power2, start, end = map(int, input().split())
bfs()
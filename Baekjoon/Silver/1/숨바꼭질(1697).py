import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    while queue:
        cur = queue.popleft()
        if cur == k:
            return visited[cur]
        for i in (cur + 1, cur - 1, cur * 2):
            if 0 <= i < MAX and not visited[i]:
                queue.append(i)
                visited[i] = visited[cur] + 1

MAX = 100001
n, k = map(int, input().split())
visited = [0] * MAX
queue = deque([n])
print(bfs())
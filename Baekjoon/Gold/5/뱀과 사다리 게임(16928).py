import sys
input = sys.stdin.readline
from collections import deque, defaultdict

def bfs():
    visited = [0, 1] + [0] * 99
    queue = deque([(1, 0)])
    while queue:
        cur, cnt = queue.popleft()
        if cur == 100:
            print(cnt)
            exit()
        for i in range(1, 7):
            if not visited[graph[cur + i]]:
                queue.append((graph[cur + i], cnt + 1))
                visited[graph[cur + i]] = 1

n, m = map(int, input().split())
graph = defaultdict(int)
for i in range(1, 101):
    graph[i] = i
for _ in range(n):
    a, b = map(int, input().split())
    graph[a] = b
for _ in range(m):
    a, b = map(int, input().split())
    graph[a] = b

bfs()
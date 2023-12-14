import sys
input = sys.stdin.readline
from collections import deque

def bfs(K, V):
    visited = [0] * (N + 1)
    visited[V] = 1
    queue = deque([V])
    cnt = 0
    while queue:
        cur = queue.popleft()
        for dot, dist in graph[cur]:
            if not visited[dot] and dist >= K:
                queue.append(dot)
                cnt += 1
                visited[dot] = 1
    return cnt

N, Q = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    p, q, r = map(int, input().split())
    graph[p] += [(q, r)]
    graph[q] += [(p, r)]

for _ in range(Q):
    k, v = map(int, input().split())
    print(bfs(k, v))
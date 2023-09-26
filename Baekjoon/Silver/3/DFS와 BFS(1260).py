import sys
from collections import deque
input = sys.stdin.readline
def dfs(v):
    visited_dfs[v] = 1
    print(v, end = " ")
    for x in graph[v]:
        if not visited_dfs[x]:
            dfs(x)

def bfs(start):
    visited_bfs[start] = 1
    queue = deque([start])
    while queue:
        cur = queue.popleft()
        print(cur, end = " ")
        for x in graph[cur]:
            if not visited_bfs[x]:
                queue.append(x)
                visited_bfs[x] = 1
                
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited_dfs, visited_bfs = [0] * (n + 1), [0] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x] += [y]
    graph[y] += [x]
    
for i in range(n + 1): # 문제 조건
    graph[i] = sorted(graph[i])

dfs(v)
print()
bfs(v)
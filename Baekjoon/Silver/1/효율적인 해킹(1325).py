import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    visited = [0] * (n + 1)
    visited[start] = 1 #i정점 꼭 방문처리 해주자....제발
    queue = deque([start])
    while queue:
        cur = queue.popleft()
        for i in graph[cur]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)
    return sum(visited) #몇개 연결되었는지 저장

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b] += [a] #문제 조건(A가 B를 신뢰한다)

ans, mx = [], 0
for i in range(1, n + 1):
    if graph[i]: #노드가 있으면 bfs 실행
        tot = bfs(i)
        ans.append([tot, i]) #결과 저장
        if mx < tot: #최대값 갱신
            mx = tot
for i in ans:
    if i[0] == mx:
        print(i[1], end = " ")
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = []
queue = deque()
for y in range(n):  #그래프 입력과 동시에 아기상어가 있는 위치를 queue에 저장
    lst = list(map(int, input().split()))
    for x in range(m):
        if lst[x]:
            queue.append([y, x])
    graph.append(lst)

#상어와 인접한 칸을 찾기 위한 좌표(상, 하, 좌, 우, 좌상, 우상, 우하, 좌하)
dx = [0, 0, -1, 1, -1, 1, 1, -1]
dy = [-1, 1, 0, 0, -1, -1, 1, 1]
while queue:
    y, x = queue.popleft()  #현재 탐색 중인 노드 큐에서 꺼냄(좌표 주의)
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        #인접한 칸이 그래프 범위 내에 있고 방문하지 않았으면
        if 0 <= nx < m and 0 <= ny < n and not graph[ny][nx]:
            graph[ny][nx] = graph[y][x] + 1 #해당 인접한 칸에 현재 칸 + 1 저장
            queue.append([ny, nx])  #인접한 칸 큐에 추가
#map(max, graph)에는 각 행 최대값들이 저장, 다시 max를 적용하여 최대값 뽑기
print(max(map(max, graph)) - 1)
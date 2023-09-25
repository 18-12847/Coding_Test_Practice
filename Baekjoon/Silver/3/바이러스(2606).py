import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    visited[start] = 1
    queue = deque([start]) #시작 정점
    while queue:
        cur = queue.popleft() #큐에서 첫번째 점을 꺼냄
        for x in graph[cur]: #해당 점에 있는 연결 정점 전부 방문 처리
            if not visited[x]: #방문 안했으면
                queue.append(x) #큐에 추가하고 방문 처리
                visited[x] = 1

computer = int(input().rstrip())
graph = [[] for _ in range(computer+1)]
visited = [0] * (computer + 1)
for i in range(int(input().rstrip())):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

bfs(1)
print(sum(visited) - 1)

# import sys
# input = sys.stdin.readline
# def dfs(v):
#     visited[v] = 1 # 해당 정점 방문 표시
#     for x in graph[v]: #각 점에 연결된 정점 확인
#         if not visited[x]: #만약 연결 되어있지않으면 깊이우선탐색
#             dfs(x)

# computer = int(input().rstrip())
# graph = [[] for _ in range(computer + 1)] #1번 인덱스부터 시작하기 위함
# visited = [0] * (computer + 1) #1번 인덱스부터 시작하기 위함
# for i in range(int(input().rstrip())):
#     a, b = map(int, input().split())
#     graph[a] += [b]
#     graph[b] += [a]
# dfs(1) #시작 정점
# print(sum(visited) - 1) #양방향 그래프로 인해 자신도 정점 방문해서 제외
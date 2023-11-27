import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    queue = deque([graph[0]]) #시작 지점 추가
    while queue:
        cx, cy = queue.popleft()
         #현재 x, y좌표랑 종료 좌표 간격이 1000 이하면 happy 반환
        if abs(cx - graph[-1][0]) + abs(cy - graph[-1][1]) <= 1000:
            return print("happy")
        for i in range(1, n + 1): #graph에서 편의점은 1부터 n번 인덱스 까지다, visited도 마찬가지
            if not visited[i]: #방문 안했으면
                nx, ny = graph[i] #해당 편의점 x, y좌표 가져오고
                if abs(cx - nx) + abs(cy - ny) <= 1000: #현재 x, y좌표랑 편의점 x, y좌표가 1000이하면
                    visited[i] = 1 #방문 표시 후 큐에 추가
                    queue.append((nx, ny))
    return print("sad")

for i in range(int(input().rstrip())):
    n = int(input().rstrip())
    graph = [tuple(map(int, input().split())) for _ in range(n + 2)]
    #편의점 개수만큼 visited 리스트 생성(1은 시작 지점 미리 체크)
    visited = [1] + [0 for _ in range(n)]
    bfs()
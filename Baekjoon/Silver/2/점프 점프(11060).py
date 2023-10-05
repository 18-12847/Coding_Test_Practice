import sys
input = sys.stdin.readline
from collections import deque

n = int(input().rstrip())
lst = list(map(int, input().split()))
visited = [n] * n
visited[0] = 0
queue = deque([0])
while queue:
    cur = queue.popleft()
    for i in range(1, lst[cur] + 1): #cur에서 최대 lst[cur]까지 점프 가능 
        if cur + i >= n: #범위 벗어나면 탈출
            break
        if visited[cur + i] == n: #방문 안했으면
						#현재 위치의 점프 횟수에 1을 더해서 방문 안한 위치의 점프 횟수 업데이트
            visited[cur + i] = visited[cur] + 1
            queue.append(cur + i) #점프한 위치를 큐에 추가
print(-1 if visited[-1] == n else visited[-1])
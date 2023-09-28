# 노션에 정리 완료
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x, y):
	#상(1, 0) 하(-1, 0) 좌(0, -1) 우(0, -1)
    dx = [0, 0, -1, 1] 
    dy = [1, -1, 0, 0]
    for i in range(4):
		#x, y의 상하좌우 좌표 nx, ny
        nx = x + dx[i]
        ny = y + dy[i]
		#좌표 기준 상하좌우에 배추가 있는지 확인
        if 0 <= nx < m and 0 <= ny < n:
            if graph[ny][nx]:
                graph[ny][nx] = 0 #있으면 재방문 안하게 뽑아버림
                dfs(nx, ny) #해당 좌표로 다시 dfs 재귀호출

for _ in range(int(input().rstrip())):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    for y in range(n):
        for x in range(m):
            if graph[y][x]:
                dfs(x, y)
                cnt += 1
    print(cnt)
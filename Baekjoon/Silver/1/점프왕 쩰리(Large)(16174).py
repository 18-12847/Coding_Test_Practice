import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(x, y):
    if [y, x] == [n - 1, n - 1]:
        print("HaruHaru")
        exit()
		#graph[y][x] 값 만큼 오른쪽, 아래로 이동 가능하므로 미리 저장
    dx = [0, graph[y][x]]
    dy = [graph[y][x], 0]
		#방문 완료 표시
    graph[y][x] = 101
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] != 101:
                dfs(nx, ny)
    
n = int(input().rstrip())
graph = [list(map(int, input().split())) for _ in range(n)]
dfs(0, 0)
print("Hing")

# def dfs(x, y):
# 		#방문 했으면 재귀 종료
#     if visited[y][x]:
#         return
#     visited[y][x] = 1
#     if x + graph[y][x] < n and not visited[y][x + graph[y][x]]:
#         dfs(x + graph[y][x], y)
#     if y + graph[y][x] < n and not visited[y + graph[y][x]][x]:
#         dfs(x, y + graph[y][x])

# n = int(input().rstrip())
# graph = [list(map(int, input().split())) for _ in range(n)]
# visited = [[0] * n for _ in range(n)]
# dfs(0, 0)
# print("HaruHaru" if visited[-1][-1] else "Hing")
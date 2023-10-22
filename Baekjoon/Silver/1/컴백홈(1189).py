#visited 배열로 방문 확인
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(x, y, depth):
    global cnt
    if depth == k and [y, x] == [0, c - 1]:
        cnt += 1
        return
    visited[y][x] = 1 #현재 위치 방문 처리
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < c and 0 <= ny < r and graph[ny][nx] == "." and not visited[ny][nx]:

            visited[ny][nx] = 1 #다음 위치 방문 처리
            dfs(nx, ny, depth + 1)
            visited[ny][nx] = 0 #재귀가 끝나면 방문 상태 원복
            
r, c, k = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
cnt = 0
dfs(0, r - 1, 1)
print(cnt)

# #그래프 자체에 방문 처리
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(100000)

# def dfs(x, y, depth):
#     global cnt
#     if depth == k and [y, x] == [0, c - 1]:
#         cnt += 1
#         return
#     graph[y][x] = "T" #현재 위치 방문 처리
#     dx = [0, 0, -1, 1]
#     dy = [-1, 1, 0, 0]
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < c and 0 <= ny < r and graph[ny][nx] == ".":
#             graph[ny][nx] = "T" #다음 위치 방문 처리
#             dfs(nx, ny, depth + 1)
#             graph[ny][nx] = "." #재귀가 끝나면 방문 상태 원복
            
# r, c, k = map(int, input().split())
# graph = [list(input().rstrip()) for _ in range(r)]
# cnt = 0
# dfs(0, r - 1, 1)
# print(cnt)
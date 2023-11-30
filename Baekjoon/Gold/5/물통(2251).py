import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    visited = [[0] * (b + 1) for _ in range(a + 1)]
    queue = deque([(0, 0, c)])
    while queue:
        x, y, z = queue.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = 1
        if not x:
            ans.append(z)

        #C -> A 물통
        if z + x > a: #C물통에서 A물통으로 옮기는데 A 물통이 넘치면
            queue.append((a, y, z - (a - x))) #C물통에서 A물통이 가득 차는데 필요한 물의 양(A - x) 만큼 빼준다
        else: #아니면 현재 물통(z) 그대로 다 옮겨준다
            queue.append((x + z, y, 0))
        #C -> B 물통
        if z + y > b: #C물통에서 B물통으로 옮기는데 B 물통이 넘치면
            queue.append((x, b, y - (b - z))) #C물통에서 B물통이 가득 차는데 필요한 물의 양(B - z) 만큼 빼준다
        else: #아니면 현재 물통(z) 그대로 다 옮겨준다
            queue.append((x, y + z, 0))

        #B -> A 물통
        if y + x > a: #B물통에서 A물통으로 옮기는데 A 물통이 넘치면
            queue.append((a, y - (a - x), z)) #B물통에서 A물통이 가득 차는데 필요한 물의 양(A - x) 만큼 빼준다
        else: #아니면 현재 물통(y) 그대로 다 옮겨준다
            queue.append((x + y, 0, z))
        #B -> C 물통
        if y + z > c: #B물통에서 C물통으로 옮기는데 C 물통이 넘치면
            queue.append((x, y - (c - z), c)) #B물통에서 C물통이 가득 차는데 필요한 물의 양(C - z) 만큼 빼준다
        else: #아니면 현재 물통(y) 그대로 다 옮겨준다
            queue.append((x, 0, z + y))

        #A -> B 물통
        if x + y > b: #A물통에서 B물통으로 옮기는데 B 물통이 넘치면
            queue.append((x - (b - y), b, z)) #A물통에서 B물통이 가득 차는데 필요한 물의 양(B - y) 만큼 빼준다
        else: #아니면 현재 물통(x) 그대로 다 옮겨준다
            queue.append((0, y + x, z))
        #A -> C 물통
        if x + z > c: #A물통에서 C물통으로 옮기는데 C 물통이 넘치면
            queue.append((x - (c - z), y, c)) #A물통에서 C물통이 가득 차는데 필요한 물의 양(C - z) 만큼 빼준다
        else: #아니면 현재 물통(x) 그대로 다 옮겨준다
            queue.append((0, y, z + x))

a, b, c = map(int, input().split())
ans = []
bfs()
print(*sorted(ans))
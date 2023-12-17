import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    while queue:
        cur = queue.popleft()
        if cur == k:
            tmp.append(visited[cur])
            continue
        for n_cur in (cur + 1, cur - 1, cur * 2):
            if 0 <= n_cur < 100001 and (not visited[n_cur] or visited[n_cur] == visited[cur] + 1):
                queue.append(n_cur)
                visited[n_cur] = visited[cur] + 1
    return tmp

n, k = map(int, input().split())
visited = [0] * 100001
queue = deque([n])
tmp = []
ans = bfs()
print(ans[0], len(ans), sep = "\n")
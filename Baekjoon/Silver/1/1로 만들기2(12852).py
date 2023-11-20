import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    visited = [0] * (n + 1)
    queue = deque([(start, str(start), 0)])
    while queue:
        cur, s, cnt = queue.popleft()
        if cur == 1:
            return print(cnt, s, sep = "\n")
        visited[cur] = 1
        m3, m2, m1 = cur // 3, cur // 2, cur - 1
        if cur / 3 == m3 and not visited[m3]:
            visited[m3] = 1
            queue.append((m3, s + " " + str(m3), cnt + 1))
        if cur / 2 == m2 and not visited[m2]:
            visited[m2] = 1
            queue.append((m2, s + " " + str(m2), cnt + 1))
        if not visited[m1]:
            visited[m1] = 1
            queue.append((m1, s + " " + str(m1), cnt + 1))

n = int(input().rstrip())
bfs(n)
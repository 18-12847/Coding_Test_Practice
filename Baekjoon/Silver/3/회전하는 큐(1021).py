import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
lst = list(map(int, input().split()))
queue = deque(range(1, n+1))
cnt = 0
for i in range(m):
    if queue[0] == lst[i]:
        queue.popleft()
        continue
    rev_queue = deque(reversed(queue))
    if queue.index(lst[i]) <= rev_queue.index(lst[i]):
        cnt += queue.index(lst[i])
        queue.rotate(-queue.index(lst[i]))
        queue.popleft()
    else:
        cnt += rev_queue.index(lst[i]) + 1
        queue.rotate(rev_queue.index(lst[i]) + 1)
        queue.popleft()
print(cnt)
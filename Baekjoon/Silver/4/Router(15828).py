import sys
from collections import deque
input = sys.stdin.readline
n = int(input().rstrip())
queue = deque()
while True:
    inp = int(input().rstrip())
    if inp == -1:
        if queue:
            print(*queue)
        else:
            print("empty")
        break
    if inp == 0:
        queue.popleft()
    else:
        if len(queue) >= n:
            continue
        else:
            queue.append(inp)
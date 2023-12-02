import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    queue = deque([(start, "")])
    while queue:
        s, op = queue.popleft()
        if s == t:
            print(op)
            exit()
        mul, plus = s * s, s + s
        if 0 <= mul <= t and mul not in check:
            queue.append((mul, op + "*"))
            check.add(mul)
        if 0 <= plus <= t and plus not in check:
            queue.append((plus, op + "+"))
            check.add(plus)
        if 1 not in check:
            queue.append((1, op + "/"))
            check.add(1)

start, t = map(int, input().split())
check = set()
check.add(start)
if start == t:
    print(0)
    exit()

bfs()
print(-1)
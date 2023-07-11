import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
queue = deque(i + 1 for i in range(n))
s = "<"
while len(queue):
    for _ in range(k - 1):
        queue.append(queue.popleft())
    s += str(queue.popleft()) + ", "
print(s[:-2] + ">")
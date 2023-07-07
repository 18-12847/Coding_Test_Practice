import sys
from collections import deque
lst = deque([i + 1 for i in range(int(sys.stdin.readline().rstrip()))])
while len(lst) != 1:
    lst.popleft()
    lst.append(lst.popleft())
print(*lst)
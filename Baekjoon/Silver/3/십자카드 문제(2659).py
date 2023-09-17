import sys
from collections import deque
input = sys.stdin.readline
queue = deque(list(map(str, input().split())))
tmp = []
for _ in range(4):
    tmp.append(int("".join(queue)))
    queue.append(queue.popleft())
cnt = 0
store = []
for i in range(1111, int(min(tmp)) + 1):
    if "0" in str(i):
        continue
    queue = deque(list(str(i)))
    ans = []
    for _ in range(4):
        ans.append(int("".join(queue)))
        queue.append(queue.popleft())
    if min(ans) not in store:
        store.append(min(ans))
        cnt += 1
print(cnt)
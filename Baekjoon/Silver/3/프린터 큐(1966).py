import sys
from collections import deque
input = sys.stdin.readline
for i in range(int(input().rstrip())):
    n, m = map(int, input().split())
    lst = deque(list(map(int, input().split())))
    for i in range(n):
        if i == m:
            lst[i] = [lst[i], True]
        else:
            lst[i] = [lst[i], False]
    cnt = 1
    while True:
        big = max(lst)
        if lst[0][0] == big[0] and lst[0][1]:
            print(cnt)
            break
        elif lst[0][0] == big[0]:
            lst.popleft()
            cnt += 1
        else:
            lst.append(lst.popleft())
import sys
from collections import deque
input = sys.stdin.readline
n = int(input().rstrip())
queue = deque(list(range(1, n + 1)))
lst = deque(list(map(int, input().split())))
for _ in range(n-1):
    tmp = lst.popleft()
    print(queue.popleft(), end=" ")
    if tmp > 0:
        queue.rotate(-tmp + 1) # 양수는 오른쪽에서 왼쪽으로 회전
        lst.rotate(-tmp + 1)
    else:
        queue.rotate(-tmp) # 음수는 왼쪽에서 오른쪽으로 회전
        lst.rotate(-tmp) # 제일 편한건 rotate를 사용하면 무조건 -를 붙이자
print(*queue)

# import sys
# from collections import deque
# input = sys.stdin.readline
# n = int(input().rstrip())
# queue = deque(list(range(1, n + 1)))
# lst = deque(list(map(int, input().split())))
# for _ in range(n-1):
#     tmp = lst.popleft()
#     print(queue.popleft(), end = " ")
#     if tmp > 0:
#         for _ in range(tmp - 1):
#             queue.append(queue.popleft())
#             lst.append(lst.popleft())
#     else:
#         for _ in range(abs(tmp)):
#             queue.appendleft(queue.pop())
#             lst.appendleft(lst.pop())
# print(*queue)
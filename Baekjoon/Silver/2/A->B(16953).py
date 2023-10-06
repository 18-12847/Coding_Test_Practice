import sys
input = sys.stdin.readline
from collections import deque

a, b = map(int, input().split())
queue = deque([[a, 1]]) #a와 연산횟수(1)로 초기화
while queue:
    cur, cnt = queue.popleft() #노드 하나 꺼낸다(현재 값, 연산 횟수)
    if cur == b: #꺼낸 현재 값이 b와 같으면 종료
        print(cnt)
        exit()
    if cur * 2 <= b: #현재 값 * 2가 b이하면 queue에 추가
        queue.append([cur * 2, cnt + 1])
    if cur * 10 + 1 <= b: #현재 값 * 10 + 1이 b이하면 queue에 추가
        queue.append([cur * 10 + 1, cnt + 1])
print(-1)
# import sys
# input = sys.stdin.readline
# a, b = map(int, input().split())
# cnt = 0
# while a <= b:
#     if a == b:
#         print(cnt + 1)
#         exit()
#     if b % 10 == 1:
#         b //= 10
#         cnt += 1
#     elif not b % 2:
#         b //= 2
#         cnt += 1
#     else:
#         print(-1)
#         exit()
# print(-1)
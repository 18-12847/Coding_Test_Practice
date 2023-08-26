import sys
input = sys.stdin.readline
n, a, b = map(int, input().split())
cnt = 0
while a != b:
    a -= a // 2
    b -= b // 2
    cnt += 1
print(cnt)
#개씨발진짜문제존나싸가지없네
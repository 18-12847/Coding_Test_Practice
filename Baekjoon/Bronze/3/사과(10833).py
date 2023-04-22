import sys
cnt = 0
for i in range(int(sys.stdin.readline().rstrip())):
    a, b = map(int, sys.stdin.readline().split())
    cnt += b % a
print(cnt)
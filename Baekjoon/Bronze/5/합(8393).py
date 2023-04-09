import sys
a = int(sys.stdin.readline())
cnt = 0
for i in range(1, a+1):
    cnt += i
print(cnt)
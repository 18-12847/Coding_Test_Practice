import sys
lst = [500, 100, 50, 10, 5, 1]
a = 1000 - int(sys.stdin.readline().rstrip())
cnt = 0
for i in lst:
    cnt += a // i
    a %= i
print(cnt)
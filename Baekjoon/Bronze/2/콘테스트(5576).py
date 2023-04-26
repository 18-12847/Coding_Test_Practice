import sys
a = sorted([int((sys.stdin.readline().rstrip())) for _ in range(10)])
b = sorted([int((sys.stdin.readline().rstrip())) for _ in range(10)])
print(sum(a[-3:]), sum(b[-3:]))
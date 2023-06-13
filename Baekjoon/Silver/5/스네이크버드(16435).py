import sys
a, b = map(int, sys.stdin.readline().split())
lst = sorted(list(map(int, sys.stdin.readline().split())))
for i in range(a):
    if b >= lst[i]:
        b += 1
print(b)
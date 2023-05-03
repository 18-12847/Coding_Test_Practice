import sys
a, b = map(int, sys.stdin.readline().split())
lst = []
for i in range(1, 1001):
    for _ in range(i):
        if len(lst) > 999:
            break
        else:
            lst.append(i)
print(sum(lst[a - 1:b]))
import sys
lst = [0, 1, 0, 0]
for i in range(int(sys.stdin.readline().rstrip())):
    a, b = map(int, sys.stdin.readline().split())
    lst[a], lst[b] = lst[b], lst[a]
print(lst.index(1))
import sys
lst = []
for i in range(5):
    lst.append(sum(list(map(int, sys.stdin.readline().split()))))
print(lst.index(max(lst)) + 1, max(lst))
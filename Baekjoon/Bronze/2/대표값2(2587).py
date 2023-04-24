import sys
lst = []
for i in range(5):
    lst.append(int(sys.stdin.readline().rstrip()))
lst.sort()
print(int(sum(lst) / 5))
print(lst[2])
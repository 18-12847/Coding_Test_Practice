import sys
lst = []
for i in range(int(sys.stdin.readline().rstrip())):
    a, b = sys.stdin.readline().split()
    lst.append([int(a), i, b])
for i in sorted(lst):
    print(i[0], i[2])
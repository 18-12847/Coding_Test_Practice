import sys
lst = []
for i in range(int(sys.stdin.readline().rstrip())):
    s = sys.stdin.readline().rstrip()
    if [len(s), s] not in lst:
        lst.append([len(s), s])
for i in sorted(lst):
    print(i[1])
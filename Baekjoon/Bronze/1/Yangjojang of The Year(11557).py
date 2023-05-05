import sys
for _ in range(int(sys.stdin.readline().rstrip())):
    lst = []
    for _ in range(int(sys.stdin.readline().rstrip())):
        lst.append(sys.stdin.readline().split())
    maxx = lst[0]
    for i in lst:
        if int(i[1]) > int(maxx[1]):
            maxx = i
    print(maxx[0])
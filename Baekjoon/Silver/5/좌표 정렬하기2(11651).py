import sys
lst = sorted([list(map(int, sys.stdin.readline().split())) for i in range(int(sys.stdin.readline().rstrip()))], key = lambda x: (x[1], x[0]))
for i in lst:
    print(*i)
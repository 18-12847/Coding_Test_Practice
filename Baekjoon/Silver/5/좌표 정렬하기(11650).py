import sys
for i in sorted([list(map(int, sys.stdin.readline().split())) for i in range(int(sys.stdin.readline().rstrip()))]):
    print(*i)
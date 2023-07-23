import sys
for _ in range(int(sys.stdin.readline().rstrip())):
    a, b = map(int, sys.stdin.readline().split())
    lst = [list(map(int, sys.stdin.readline().split())) for _ in range(b)]
    print(a - 1)
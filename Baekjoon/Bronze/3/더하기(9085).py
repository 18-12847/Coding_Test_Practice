import sys
for i in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    print(sum(list(map(int, sys.stdin.readline().split()))))
import sys
for i in range(int(sys.stdin.readline())):
    print(sorted(list(map(int, sys.stdin.readline().split())))[-3])
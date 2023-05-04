import sys
for i in range(int(sys.stdin.readline().rstrip())):
    lst = sys.stdin.readline().split()
    for j in lst:
        print(j[::-1], end = " ")
    print()
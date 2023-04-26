import sys
for i in range(int(sys.stdin.readline().rstrip())):
    maxx = 0
    for j in range(int(sys.stdin.readline().rstrip())):
        a, b = sys.stdin.readline().split()
        if maxx < int(a):
            maxx, s = int(a), b
    print(s)
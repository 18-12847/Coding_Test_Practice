import sys
for i in range(int(sys.stdin.readline().rstrip())):
    a, b = sys.stdin.readline().split()
    print(b[:int(a) - 1] + b[int(a):])
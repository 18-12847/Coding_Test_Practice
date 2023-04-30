import sys
for i in range(int(sys.stdin.readline().rstrip())):
    a, b = sys.stdin.readline().split()
    if sorted(list(a)) == sorted(list(b)):
        print("Possible")
    else:
        print("Impossible")
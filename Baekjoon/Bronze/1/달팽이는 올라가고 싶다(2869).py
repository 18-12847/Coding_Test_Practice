import sys
a, b, v = map(int, sys.stdin.readline().split())
if a >= v:
    print("1")
elif a - b >= v - a:
    print("2")
else:
    print((v - a) // (a - b) + 2 if (v - a) % (a - b) else (v - a) // (a - b) + 1)
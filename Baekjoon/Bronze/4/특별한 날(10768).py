import sys
a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
if a * 100 + b > 218:
    print("After")
elif a * 100 + b == 218:
    print("Special")
else:
    print("Before")
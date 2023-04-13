import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
if a == b == c and a + b + c == 180:
    print("Equilateral")
elif (a == b or a == c or b == c) and a + b + c == 180:
    print("Isosceles")
elif a + b + c == 180:
    print("Scalene")
else:
    print("Error")
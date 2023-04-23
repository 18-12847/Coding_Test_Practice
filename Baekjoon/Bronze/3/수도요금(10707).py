import sys
a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
c = int(sys.stdin.readline().rstrip())
d = int(sys.stdin.readline().rstrip())
p = int(sys.stdin.readline().rstrip())
print(min(a * p, b if c >= p else (p - c) * d + b))
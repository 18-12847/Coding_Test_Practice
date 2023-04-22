import sys
n = sys.stdin.readline().rstrip()
op = sys.stdin.readline().rstrip()
m = sys.stdin.readline().rstrip()
n += (op + m)
print(eval(n))
import sys
n = int(sys.stdin.readline().rstrip())
[print(" " * i + "*" * (n - i)) for i in range(n)]
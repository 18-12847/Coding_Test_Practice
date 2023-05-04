import sys
x, y = sys.stdin.readline().split()
print(int(str(int(x[::-1]) + int(y[::-1]))[::-1]))
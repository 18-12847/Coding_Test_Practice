import sys
n, k = map(int, sys.stdin.readline().split())
m = sorted(list(map(int, sys.stdin.readline().split())), reverse = True)
print(m[k-1])
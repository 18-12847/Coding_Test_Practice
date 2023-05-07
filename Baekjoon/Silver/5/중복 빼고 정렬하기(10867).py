import sys
n = int(sys.stdin.readline().rstrip())
print(*sorted(list(set(list(map(int, sys.stdin.readline().split()))))))
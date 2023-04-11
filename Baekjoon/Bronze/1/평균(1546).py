import sys
n = int(sys.stdin.readline())
total = list(map(int, sys.stdin.readline().split()))
print(sum(total) / max(total) * 100 / n)
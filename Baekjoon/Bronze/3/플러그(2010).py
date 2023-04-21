import sys
tot = 0
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    tot += int(sys.stdin.readline().rstrip())
print(tot - (n - 1))
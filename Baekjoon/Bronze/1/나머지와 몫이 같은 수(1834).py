import sys
n = int(sys.stdin.readline().rstrip())
tot = 0
for i in range(1, n):
    tot += (n + 1) * i
print(tot)
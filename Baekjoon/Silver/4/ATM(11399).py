import sys
n = int(sys.stdin.readline().rstrip())
tot = 0
lst = sorted(list(map(int, sys.stdin.readline().split())))
for i in range(n):
    tot += sum(lst[:i + 1])
print(tot)
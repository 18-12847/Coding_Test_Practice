import sys
a, b = sys.stdin.readline().split()
a, b = list(map(int, a)), list(map(int, b))
tot = 0
for i in a:
    tot += sum(b) * i
print(tot)
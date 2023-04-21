import sys
tot = int(sys.stdin.readline().rstrip())
for _ in range(9):
    tot -= int(sys.stdin.readline().rstrip())
print(tot)
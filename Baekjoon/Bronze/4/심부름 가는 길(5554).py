import sys
tot = 0
for _ in range(4):
    tot += int(sys.stdin.readline())
print(tot // 60, tot % 60, sep="\n")
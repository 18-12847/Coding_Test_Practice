import sys
s = sys.stdin.readline().rstrip()
tot = 0
for i in s:
    tot += int(i) ** 5
print(tot)
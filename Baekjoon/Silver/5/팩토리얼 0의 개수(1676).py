import sys
tot = 1
for i in range(1, int(sys.stdin.readline().rstrip()) + 1):
    tot *= i
print(len(list(str(tot))) - len(str(tot).rstrip("0")))
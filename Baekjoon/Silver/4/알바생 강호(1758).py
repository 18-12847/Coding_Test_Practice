import sys
input = sys.stdin.readline
lst = sorted([int(input().rstrip()) for _ in range(int(input().rstrip()))])[::-1]
tot = 0
for i in range(len(lst)):
    if lst[i] - i < 0:
        break
    else:
        tot += lst[i] - i
print(tot)
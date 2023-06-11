import sys
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().split()))
tot = 0
for i in lst:
    m -= 1
    tot += i * (a ** m)
tmp = []
while tot > b - 1:
    tmp.append(tot % b)
    tot //= b
print(tot, *list(reversed(tmp)))
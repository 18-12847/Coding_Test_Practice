import sys
n = int(sys.stdin.readline().rstrip())
lst1 = sorted(list(map(int, sys.stdin.readline().split())), reverse = True)
lst2 = sorted(list(map(int, sys.stdin.readline().split())))
tot = 0
for i in range(n):
    tot += lst1[i] * lst2[i]
print(tot)
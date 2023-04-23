import sys
tot = 0
lst = []
for i in range(10):
    n, m = map(int, sys.stdin.readline().split())
    tot -= n
    tot += m
    lst.append(tot)
print(max(lst))
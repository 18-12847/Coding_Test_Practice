import sys
a = list(map(int, sys.stdin.readline().split()))
if len(list(set(a))) == 1:
    print(10000 + a[0] * 1000)
elif len(list(set(a))) == 2:
    print(1000 + sorted(a)[1] * 100)
else:
    print(max(a) * 100)
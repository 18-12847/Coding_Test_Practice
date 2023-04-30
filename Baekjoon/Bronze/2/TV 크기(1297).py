import sys
d, h, w = map(int, sys.stdin.readline().split())
d = d ** 2
tmp = h ** 2 + w ** 2
d = (d / tmp) ** 0.5
print(int(d * h), int(d * w))
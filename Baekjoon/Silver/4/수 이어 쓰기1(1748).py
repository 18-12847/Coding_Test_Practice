import sys
input = sys.stdin.readline
n = int(input().rstrip())
a, cnt, tot = n, len(str(n)) - 1, 0
while a > 10:
    tmp = a - (10 ** cnt) + 1
    tot += tmp * (cnt + 1)
    a, cnt = a - tmp, cnt - 1
print(tot + 9 if n > 10 else n)
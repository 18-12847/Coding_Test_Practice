import sys
a, b, c = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
a += n // 3600
b += (n - (n // 3600 * 3600)) // 60
c += n % 60
if c > 59:
    b += 1
    c %= 60
if b > 59:
    a += 1
    b %= 60
if a > 23:
    a %= 24
print(a, b, c)
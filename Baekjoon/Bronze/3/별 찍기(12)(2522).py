import sys
n = int(sys.stdin.readline().rstrip())
for i in range(1, 2 * n):
    if i <= n:
        print((n - i) * " " + i * "*")
    else:
        print((i - n) * " " + (n * 2 - i) * "*")
import sys
n = int(sys.stdin.readline().rstrip())
for i in range(1, n * 2):
    if i <= n:
        print((n - i) * " " + (i * 2 - 1) * "*")
    else:
        print((i - n) * " " + ((n - (i - n)) * 2 - 1) * "*")
import sys
n = int(sys.stdin.readline().rstrip())
for i in range(1, n * 2):
    if i < n:
        print((i - 1) * " " + ((n - i) * 2 + 1) * "*")
    elif i == n:
        print((n - 1) * " " + "*")
    else:
        print((n * 2 - 1 - i) * " " + ((i - n) * 2 + 1) * "*")
import sys
n = int(sys.stdin.readline().rstrip())
for i in range(1, n * 2):
    if i < n:
        print(i * "*" + ((n - i) * 2) * " " + i * "*")
    elif i == n:
        print("*" * (2 * n))
    else:
        print((((2 * n) - 1) - i + 1) * "*" + ((i - n) * 2) * " " + (((2 * n) - 1) - i + 1) * "*")
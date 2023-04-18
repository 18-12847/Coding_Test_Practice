import sys
n = int(sys.stdin.readline().rstrip())
for i in range(1, n * 2):
    if i <= n:
        print(i * "*")
    else:
        print((n * 2 - i) * "*")
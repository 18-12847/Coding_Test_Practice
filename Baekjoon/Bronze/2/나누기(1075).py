import sys
n = int(sys.stdin.readline().rstrip())
f = int(sys.stdin.readline().rstrip())
n = n - (n % 100)
for i in range(n, n + 100):
    if i % f == 0:
        print(str(i)[-2:])
        break
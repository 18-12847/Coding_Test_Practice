import sys
for _ in range(int(sys.stdin.readline().rstrip())):
    h, w, n = map(int, sys.stdin.readline().split())
    if n % h == 0:
        print(str(h) + str(n // h).zfill(2))
    else:
        print(str(n % h) + str(int(n / h) + 1).zfill(2))
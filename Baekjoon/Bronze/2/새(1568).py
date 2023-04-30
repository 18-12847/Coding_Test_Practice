import sys
n = int(sys.stdin.readline().rstrip())
cnt, tot = 0, 1
for _ in range(n):
    if n <= 0:
        break
    elif n == tot:
        n -= tot
        tot = 1
        tot += 1
        cnt += 1
    elif n < tot:
        tot = 1
        n -= tot
        tot += 1
        cnt += 1
    else:
        n -= tot
        tot += 1
        cnt += 1
print(cnt)    
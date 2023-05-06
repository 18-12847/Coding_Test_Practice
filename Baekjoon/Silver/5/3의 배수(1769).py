import sys
n = list(map(int, sys.stdin.readline().rstrip()))
if len(n) == 1:
    print("0")
    print("NO" if sum(n) % 3 else "YES")
else:
    cnt = 1
    while sum(n) > 9:
        n = list(map(int, str(sum(n))))
        cnt += 1
    print(cnt)
    print("NO" if sum(n) % 3 else "YES")
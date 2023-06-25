import sys
n, k = map(int, sys.stdin.readline().split())
lst = sorted([int(sys.stdin.readline().rstrip()) for _ in range(n)], reverse = True)
cnt = 0
for i in lst:
    cnt += k // i
    k = k % i
print(cnt)
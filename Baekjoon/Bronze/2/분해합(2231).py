import sys
n = int(sys.stdin.readline().rstrip())
ans = 0
for i in range(n + 1):
    if i + sum(list(map(int, str(i)))) == n:
        ans = i
        break
print(ans)
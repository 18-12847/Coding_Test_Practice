import sys
n = int(sys.stdin.readline().rstrip())
cnt = 0
for i in range(1, n + 1):
    for j in range(i, n // i + 1):
        cnt += 1
print(cnt)
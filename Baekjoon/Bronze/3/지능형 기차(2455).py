import sys
ans = [0] * 4
for i in range(4):
    a, b = map(int, sys.stdin.readline().split())
    if i == 0:
        ans[i] = b
    else:
        ans[i] = ans[i-1] + b - a
print(max(ans))
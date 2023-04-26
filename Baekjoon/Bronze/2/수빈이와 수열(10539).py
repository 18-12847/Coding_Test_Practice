import sys
a = int(sys.stdin.readline().rstrip())
b = list(map(int, sys.stdin.readline().split()))
ans = [b[0]]
print(b[0], end = " ")
for i in range(1, len(b)):
    ans.append(b[i] * (i + 1) - sum(ans[:i]))
    print(b[i] * (i + 1) - sum(ans[:i]), end = " ")
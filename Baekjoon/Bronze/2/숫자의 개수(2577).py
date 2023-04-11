import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
tot = a * b * c
ans = [0] * 10
for i in list(str(tot)):
    ans[int(i)] += 1
print(*ans, sep = "\n")
import sys
ans = []
for i in range(7):
    a = int(sys.stdin.readline().rstrip())
    if a % 2:
        ans.append(a)
if len(ans) > 0:
    print(sum(ans), min(ans), sep = "\n")
else:
    print("-1")
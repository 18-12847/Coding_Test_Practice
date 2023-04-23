import sys
n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().split()))
y, m = [], []
for i in range(n):
    y.append((lst[i] // 30 * 10) + 10)
    m.append((lst[i] // 60 * 15) + 15)
if sum(y) == sum(m):
    print(f"Y M {sum(y)}")
else:
    if sum(y) > sum(m):
        print(f"M {sum(m)}")
    else:
        print(f"Y {sum(y)}")
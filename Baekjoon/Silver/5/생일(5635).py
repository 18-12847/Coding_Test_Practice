import sys
lst = []
for i in range(int(sys.stdin.readline().rstrip())):
    a, b, c, d = sys.stdin.readline().split()
    s = [d.zfill(4) + c.zfill(2) + b.zfill(2), a]
    lst.append(s)
print(sorted(lst)[-1][1], sorted(lst)[0][1], sep = "\n")
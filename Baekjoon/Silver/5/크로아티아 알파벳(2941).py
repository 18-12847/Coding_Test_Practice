import sys
lst = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
s = sys.stdin.readline().rstrip()
for i in lst:
    s = s.replace(i, ".")
print(len(s))
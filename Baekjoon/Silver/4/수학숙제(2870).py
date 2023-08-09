import sys
input = sys.stdin.readline
lst = [ input().rstrip() for i in range(int(input().rstrip()))]
ans = []
for i in lst:
    s = ""
    for j in i:
        if j.isalpha():
            s += " "
        else:
            s += j
    s = s.split()
    for j in s:
        ans.append(int(j))
print(*sorted(ans), sep = "\n")
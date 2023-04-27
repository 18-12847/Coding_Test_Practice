import sys
ans, lst = "", []
for i in range(int(sys.stdin.readline().rstrip())):
    lst.append(sys.stdin.readline().rstrip()[0])
tmp = sorted(set(lst))
for i in tmp:
    if lst.count(i) > 4:
        ans += i
print(ans if ans else "PREDAJA")
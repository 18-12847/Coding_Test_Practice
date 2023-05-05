import sys
n = int(sys.stdin.readline().rstrip())
ans = []
for i in range(4, n + 1):
    if sorted(list(set(list(str(i))))) == ["4"] or sorted(list(set(list(str(i))))) == ["7"] or sorted(list(set(list(str(i))))) == ["4", "7"]:
        ans.append(i)
print(ans[-1])
import sys
lst = [sys.stdin.readline().rstrip() for i in range(int(sys.stdin.readline().rstrip()))]
ans = list(lst[0])
for i in lst:
    for idx, val in enumerate(i):
        if ans[idx] != val:
            ans[idx] = "?"
print("".join(ans))
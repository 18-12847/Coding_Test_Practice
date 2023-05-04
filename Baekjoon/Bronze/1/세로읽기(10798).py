import sys
lst = [sys.stdin.readline().rstrip() for _ in range(5)]
ans = [len(i) for i in lst]
for i in range(5):
    lst[i] = lst[i].ljust(max(ans))
for i in range(max(ans)):
    for j in range(5):
        if lst[j][i] != " ":
            print(lst[j][i], end = "")
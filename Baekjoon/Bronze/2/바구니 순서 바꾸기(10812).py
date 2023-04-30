import sys
n, m = map(int, sys.stdin.readline().split())
lst = [i + 1 for i in range(n)]
for i in range(m):
    begin, end, mid = map(int, sys.stdin.readline().split())
    tmp = lst[begin - 1 : end]
    for i in range(mid - begin):
        tmp.append(tmp.pop(0))
    for i in range(len(tmp)):
        lst[i + begin - 1] = tmp[i]
print(*lst)
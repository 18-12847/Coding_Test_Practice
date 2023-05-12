import sys
n = int(sys.stdin.readline().rstrip())
lst = [i + 1 for i in range(n)]
for i in range(n-1):
    print(lst[0], end = " ")
    lst.pop(0)
    lst.append(lst.pop(0))
print(*lst)
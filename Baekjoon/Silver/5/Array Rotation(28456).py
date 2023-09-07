import sys
input = sys.stdin.readline
n = int(input().rstrip())
lst = [list(map(int, input().split())) for _ in range(n)]
op = [input().split() for _ in range(int(input().rstrip()))]
for i in op:
    if len(i) > 1:
        lst[int(i[1])-1].insert(0, lst[int(i[1])-1].pop())  
    else:
        lst = list(map(list, zip(*lst)))
        for i in range(n):
            lst[i] = lst[i][::-1]
for i in lst:
    print(*i)
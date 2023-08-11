import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst = [list(input().rstrip()) for _ in range(n)]
tot = 0
for i in lst:
    i = "".join(i).split("|")
    for j in i:
        if len(j) > 0:
            tot += 1
lst2 = list(map(list, zip(*lst))) #리스트 90도 돌리는 방법
for i in lst2:
    i = "".join(i).split("-")
    for j in i:
        if len(j) > 0:
            tot += 1
print(tot)
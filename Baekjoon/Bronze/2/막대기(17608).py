import sys
lst = [int(sys.stdin.readline().rstrip()) for i in range(int(sys.stdin.readline().rstrip()))][::-1]
cnt, maxx = 1, lst[0]
for i in range(1, len(lst)):
    if lst[i] > maxx:
        cnt += 1
        maxx = lst[i]
print(cnt)
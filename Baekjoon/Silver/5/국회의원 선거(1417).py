import sys
lst = [int(sys.stdin.readline().rstrip()) for _ in range(int(sys.stdin.readline().rstrip()))]
if len(lst) == 1:
    print(0)
    sys.exit()
tmp, cnt = lst[0], 0
lst = lst[1:]
while tmp <= max(lst):
    lst = sorted(lst, reverse = True)
    lst.append(lst.pop(0) - 1)
    tmp += 1
    cnt += 1
print(cnt)
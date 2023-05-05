import sys
lst = [int(sys.stdin.readline().rstrip()) for _ in range(10)]
tmp = [abs(sum(lst[:i + 1]) - 100) for i in range(10)]
for idx, val in enumerate(tmp):
    if val == min(tmp):
        ans = idx
print(sum(lst[:ans + 1]) if sum(lst) > 100 else sum(lst))
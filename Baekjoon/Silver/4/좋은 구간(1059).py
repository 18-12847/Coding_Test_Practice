import sys
input = sys.stdin.readline
a = int(input().rstrip())
lst = sorted(list(map(int, input().split())))
n = int(input().rstrip())
tot = 0
if a == 1:
    print(lst[0] - n - 1)
    exit()
for i in range(a-1):
    if lst[i] == n:
        tot = 0
        break
    elif lst[i] <= n < lst[i + 1]:
        tot += (n - lst[i] - 1) * (lst[i+1] - n - 1) + (lst[i+1] - lst[i] - 2)
        break
    elif 0 < n < lst[i]:
        tot += (n * (lst[i] - n) - 1)
        break
print(tot)
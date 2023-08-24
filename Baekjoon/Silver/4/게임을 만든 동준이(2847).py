import sys
input = sys.stdin.readline
lst = [int(input().rstrip()) for _ in range(int(input().rstrip()))][::-1]
tot = 0
for i in range(1, len(lst)):
    if lst[i] >= lst[i-1]:
        tot += (lst[i] - lst[i-1] + 1)
        lst[i] -= lst[i] - lst[i-1] + 1
print(tot)
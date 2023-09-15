import sys
input = sys.stdin.readline
n = int(input().rstrip())
lst = sorted(list(map(int, input().split())))
lst_tot = [0]
for i in range(n):
    lst_tot.append(lst_tot[-1] + lst[i])
ans = []
for i in range(n):
    l_sum, r_sum = lst_tot[i], lst_tot[-1] - lst_tot[i]
    tot = (i * lst[i] - l_sum) + (r_sum - (n - i) * lst[i])
    ans.append([tot, lst[i]])
print(min(ans)[1])

# print(lst[n//2] if n % 2 else lst[n//2-1])
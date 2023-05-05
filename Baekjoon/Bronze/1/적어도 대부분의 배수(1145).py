import sys, math
lst = list(map(int, sys.stdin.readline().split()))
tot = []
for i in range(3):
    for j in range(1, 4):
        for k in range(2, 5):
            gcd = math.gcd(lst[i], lst[j])
            lcm = lst[i] * lst[j] / gcd
            gcd = math.gcd(int(lcm), lst[k])
            tot.append(int(lcm * lst[k] / gcd))
ans = []
for i in sorted(list(set(tot))):
    cnt = 0
    for j in lst:
        if i % j == 0:
            cnt += 1
    if cnt > 2:
        ans.append(i)
print(ans[0])
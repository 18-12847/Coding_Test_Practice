import sys
n, m = map(int, sys.stdin.readline().split())
lst1, lst2 = [0, n], [0, m]
for _ in range(int(sys.stdin.readline().rstrip())):
    a, b = map(int, sys.stdin.readline().split())
    if a:
        lst1.append(b)
    else:
        lst2.append(b)
lst1.sort(), lst2.sort()
tot = 0
for i in range(1, len(lst1)):
    for j in range(1, len(lst2)):
        tmp = (lst1[i] - lst1[i - 1]) * (lst2[j] - lst2[j - 1])
        if tmp > tot:
            tot = tmp
print(tot)
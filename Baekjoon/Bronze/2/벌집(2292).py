import sys
n = int(sys.stdin.readline().rstrip())
lst = [[1, 2, 0]]
i, cnt = 2, 0
while i <= n:
    cnt += 1
    lst.append([i, i + 6 * cnt, cnt])
    i += 6 * cnt
for i in lst:
    if i[0] <= n < i[1]:
        print(i[2] + 1)
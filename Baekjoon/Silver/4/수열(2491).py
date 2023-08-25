import sys
input = sys.stdin.readline
n = int(input().rstrip())
lst = list(map(int, input().split()))
ans, tot, cnt = [], 0, 0
for i in lst:
    if i >= tot:
        cnt += 1
        tot = i
    elif i < tot and cnt > 0:
        ans.append(cnt)
        tot, cnt = i, 1
ans.append(cnt)
tot, cnt = 0, 0
for i in lst[::-1]:
    if i >= tot:
        cnt += 1
        tot = i
    elif i < tot and cnt > 0:
        ans.append(cnt)
        tot, cnt = i, 1
ans.append(cnt)
print(max(ans))
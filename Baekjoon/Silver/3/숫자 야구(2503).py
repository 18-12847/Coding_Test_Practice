#에휴..
import sys
input = sys.stdin.readline
n = int(input().rstrip())
lst = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
for i in range(123, 988):
    tmp = str(i)
    if "0" in tmp or len(set(tmp)) != 3:
        continue
    for j in range(n):
        strike, ball = 0, 0
        num = list(str(lst[j][0]))
        s, b = lst[j][1], lst[j][2]
        for k in range(3):
            if tmp[k] == num[k]:
                strike += 1
            elif tmp[k] in num:
                ball += 1
        if strike != s or ball != b:
            break
    else:
        cnt += 1
print(cnt)
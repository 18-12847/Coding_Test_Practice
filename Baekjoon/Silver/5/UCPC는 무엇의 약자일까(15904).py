import sys
s = sys.stdin.readline().rstrip()
cnt, ans = 0, "UCPC"
for i in s:
    if i == ans[cnt]:
        cnt += 1
        if cnt == 4:
            break
if cnt == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")
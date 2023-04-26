import sys
ans = ""
for i in range(50):
    ans += sys.stdin.readline().rstrip()
ans = ans.replace(" ", "")
tmp = "abcdefghijklmnopqrstuvwxyz"
cnt = []
for i in tmp:
    cnt.append(ans.count(i))
for idx, val in enumerate(cnt):
    if val == max(cnt):
        print(tmp[idx], end = "")
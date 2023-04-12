import sys
a = sys.stdin.readline().rstrip().upper()
dic = {}
for i in a:
    dic[i] = 0
for i in a:
    dic[i] += 1
maxx = max(dic.values())
cnt = 0
for i in dic:
    if dic[i] == maxx:
        cnt += 1
for k, v in dic.items():
    if cnt == 1 and v == maxx:
        print(k)
        break
    elif cnt > 1:
        print("?")
        break
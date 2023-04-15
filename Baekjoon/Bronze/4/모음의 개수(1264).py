import sys
while True:
    cnt = 0
    s = sys.stdin.readline().rstrip()
    if s == "#":
        break
    for i in s:
        if i.lower() in ["a", "e", "i", "o", "u"]:
            cnt += 1
    print(cnt)
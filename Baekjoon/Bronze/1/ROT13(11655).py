import sys
s = sys.stdin.readline().rstrip()
ans = list("abcdefghijklmnopqrstuvwxyz")
for i in s:
    if i.islower():
        print(ans[(ans.index(i) + 13) % len(ans)], end = "")
    elif i == " ":
        print(" ", end = "")
    elif i.isdigit():
        print(i, end = "")
    else:
        print(ans[(ans.index(i.lower()) + 13) % len(ans)].upper(), end = "")
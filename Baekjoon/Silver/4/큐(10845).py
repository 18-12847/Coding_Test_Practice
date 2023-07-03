import sys
lst = []
for i in range(int(sys.stdin.readline().rstrip())):
    s = list(sys.stdin.readline().split())
    if len(s) == 1:
        if s[0] == "front":
            print(lst[0] if len(lst) else -1)
        elif s[0] == "back":
            print(lst[-1] if len(lst) else -1)
        elif s[0] == "size":
            print(len(lst))
        elif s[0] == "empty":
            print(0 if len(lst) else 1)
        elif s[0] == "pop":
            print(lst.pop(0) if len(lst) else -1)
    else:
        lst.append(s[1])
import sys
while True:
    lst, tmp = [], []
    s = sys.stdin.readline().rstrip()
    if s == ".":
        break
    for i in s:
        if i in ["(", ")", "[", "]"]:
            lst.append(i)
    for i in lst:
        if i == "(":
            tmp.append(i)
        elif i == ")" and tmp and tmp[-1] == "(":
            tmp.pop()
        elif i == "[":
            tmp.append(i)
        elif i == "]" and tmp and tmp[-1] == "[":
            tmp.pop()
        else:
            tmp.append(i)
    print("no" if tmp else "yes")
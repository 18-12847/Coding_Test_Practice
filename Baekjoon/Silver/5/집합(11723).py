import sys
s = set()
for i in range(int(sys.stdin.readline().rstrip())):
    inp = sys.stdin.readline().split()
    if len(inp) == 1:
        a = inp[0]
    else:
        a, b = inp[0], int(inp[1])
    if a == "add" and b not in s:
        s.add(b)
    elif a == "remove" and b in s:
        s.remove(b)
    elif a == "check":
        print(1 if b in s else 0)
    elif a == "toggle":
        if b in s:
            s.remove(b)
        else:
            s.add(b)
    elif a == "all":
        s = set(i for i in range(1, 21))
    else:
        s = set()
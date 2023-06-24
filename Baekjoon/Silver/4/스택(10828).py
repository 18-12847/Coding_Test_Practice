import sys
stack = []
for i in range(int(sys.stdin.readline().rstrip())):
    s = sys.stdin.readline().rstrip()
    if len(s.split()) == 1:
        a = s
    else:
        s = s.split()
        a, b = s[0], s[1]
    if a == "push":
        stack.append(b)
    elif a == "top":
        if stack:
            print(stack[-1])
        else:
            print("-1")
    elif a == "size":
        print(len(stack))
    elif a == "empty":
        if stack:
            print("0")
        else:
            print("1")
    else:
        if stack:
            print(stack.pop())
        else:
            print("-1")
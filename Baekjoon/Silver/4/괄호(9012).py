import sys
for i in range(int(sys.stdin.readline().rstrip())):
    s = sys.stdin.readline().rstrip()
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        elif stack[-1] == i:
            stack.append(i)
        elif stack[-1] == ")" and i == "(":
            stack.append(i)
        else:
            stack.pop()
    print("NO" if stack else "YES")
import sys
input = sys.stdin.readline
s = input().rstrip()
stack = []
flag = False
ans = ""
for i in s:
    if flag or i == "<" or i == " ":
        if stack:
            ans += "".join(stack[::-1])
            stack = []
        ans += i
        if i == ">":
            flag = False
        if i == "<":
            flag = True
    else:
        stack.append(i)
if stack:
    ans += "".join(stack[::-1])
print(ans)
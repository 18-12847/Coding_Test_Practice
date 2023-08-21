import sys
input = sys.stdin.readline
cnt = 0
for i in range(int(input().strip())):
    stack, flag = [], False
    s = input().rstrip()
    for i in s:
        if not stack:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
            flag = True
        else:
            stack.append(i)
    if stack:
        flag = False
    else:
        if flag:
            cnt += 1
print(cnt)
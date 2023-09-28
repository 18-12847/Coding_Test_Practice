import sys
input = sys.stdin.readline
n = int(input().rstrip())
stack, ans = [], []
i = 1
for _ in range(n):
    num = int(input().rstrip())
    while i <= num:
        stack.append(i)
        ans.append("+")
        i += 1
    if stack[-1] == num:
        ans.append("-")
        stack.pop()
    else:
        print("NO")
        exit()
print(*ans, sep = "\n")
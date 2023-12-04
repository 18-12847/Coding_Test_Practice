import sys
input = sys.stdin.readline
n = int(input().rstrip())
lst = list(map(int, input().split()))
stack = []
for idx, val in enumerate(lst):
    while stack and stack[-1][1] < val:
        stack.pop()
    if stack:
        print(stack[-1][0] + 1, end = " ")
    else:
        print(0, end = " ")
    stack.append((idx, val))
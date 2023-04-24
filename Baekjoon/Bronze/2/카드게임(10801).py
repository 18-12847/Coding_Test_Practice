import sys
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
a_w, b_w = 0, 0
for i in zip(a, b):
    if i[0] > i[1]:
        a_w += 1
    elif i[0] < i[1]:
        b_w += 1
if a_w > b_w:
    print("A")
elif a_w < b_w:
    print("B")
else:
    print("D")
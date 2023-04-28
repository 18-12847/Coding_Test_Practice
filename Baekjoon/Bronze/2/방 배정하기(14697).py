import sys
a, b, c, n = map(int, sys.stdin.readline().split())
flag = False
for i in range(51):
    for j in range(51):
        for k in range(51):
            if i * a + j * b + k * c == n:
                flag = True
                break
print(1 if flag else 0)
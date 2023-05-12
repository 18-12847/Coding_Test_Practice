import sys
n = int(sys.stdin.readline().rstrip())
lst = [1, 1]
for i in range(2, n + 1):
    lst.append(lst[i-2] + lst[i-1])
print((lst[-1] + lst[-2]) * 2)
import sys
n = int(sys.stdin.readline().rstrip())
lst = [1, 1, 1]
for i in range(3, n):
    lst.append(lst[i-1] + lst[i-3])
print(lst[-1])
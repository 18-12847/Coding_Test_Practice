import sys
n = int(sys.stdin.readline().rstrip())
lst = [0, 1]
for i in range(2, 91):
    lst.append(lst[i - 2] + lst[i - 1])
print(lst[n])
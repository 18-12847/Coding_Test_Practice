import sys
lst = [0, 1]
for i in range(2, int(sys.stdin.readline().rstrip()) + 1):
    lst.append(lst[i - 2] + lst[i - 1])
print(lst[-1])
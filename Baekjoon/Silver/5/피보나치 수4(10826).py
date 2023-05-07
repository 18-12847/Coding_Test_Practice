import sys
lst = [0, 1]
n = int(sys.stdin.readline().rstrip())
for i in range(2, n + 1):
    lst.append(lst[i-1] + lst[i - 2])
print(lst[-1] if n > 2 else lst[n])
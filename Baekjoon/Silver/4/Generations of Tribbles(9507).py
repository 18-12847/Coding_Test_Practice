import sys
for i in range(int(sys.stdin.readline().rstrip())):
    lst = [1, 1, 2, 4]
    n = int(sys.stdin.readline().rstrip())
    if n < 4:
        print(lst[n])
    else:
        for i in range(4, n + 1):
            lst.append(lst[i-4] + lst[i-3] + lst[i-2] + lst[i-1])
        print(lst[-1])
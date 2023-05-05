import sys
lst = list(map(int, sys.stdin.readline().split()))
for i in range(4):
    for j in range(4):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
            print(*lst)
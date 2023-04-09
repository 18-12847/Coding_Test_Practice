import sys
a, b = map(int, sys.stdin.readline().split())
arr1 = [list(map(int, sys.stdin.readline().split())) for _ in range(a)]
arr2 = [list(map(int, sys.stdin.readline().split())) for _ in range(a)]
for i in range(len(arr1)):
    for j in range(len(arr1[i])):
        arr1[i][j] += arr2[i][j]
for i in range(len(arr1)):
    print(*arr1[i], sep=" ")
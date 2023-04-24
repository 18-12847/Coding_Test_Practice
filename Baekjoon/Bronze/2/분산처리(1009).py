import sys
lst = [[1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6],
      [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1], [10]]
for i in range(int(sys.stdin.readline().rstrip())):
    a, b = map(int, sys.stdin.readline().split())
    print(lst[a % 10 - 1][b % len(lst[a % 10 - 1]) - 1])
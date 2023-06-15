import sys
n = int(sys.stdin.readline().rstrip())
lst = sorted(list(map(int, sys.stdin.readline().split())), reverse = True)
tmp = [i + 2 + lst[i] for i in range(n)]
print(max(tmp))
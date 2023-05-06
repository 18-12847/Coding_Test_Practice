import sys
lst = [int(sys.stdin.readline().rstrip()) for i in range(int(sys.stdin.readline().rstrip()))]
print(*sorted(lst), sep = "\n")
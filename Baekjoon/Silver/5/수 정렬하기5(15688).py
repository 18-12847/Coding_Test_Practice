import sys
print(*sorted([int(sys.stdin.readline().rstrip()) for i in range(int(input().rstrip()))]), sep = "\n")
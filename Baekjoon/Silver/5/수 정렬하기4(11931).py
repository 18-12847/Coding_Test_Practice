import sys
print(*sorted([int(sys.stdin.readline().rstrip()) for _ in range(int(sys.stdin.readline().rstrip()))])[::-1], sep = "\n")
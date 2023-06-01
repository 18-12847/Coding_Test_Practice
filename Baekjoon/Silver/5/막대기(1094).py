import sys
print(bin(int(sys.stdin.readline().rstrip()))[2:].count("1"))
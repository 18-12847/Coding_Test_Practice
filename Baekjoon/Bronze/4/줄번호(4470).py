import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    s = sys.stdin.readline().rstrip()
    print(f"{i+1}. {s}")
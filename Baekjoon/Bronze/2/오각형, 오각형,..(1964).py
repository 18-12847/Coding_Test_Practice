import sys
n = int(sys.stdin.readline().rstrip())
if n == 1:
    print("5")
else:
    print(int(5 + 7 * (n - 1) + 3 * ((n - 1) * (n - 2)) / 2) % 45678)
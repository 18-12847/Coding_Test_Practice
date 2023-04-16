import sys
n = int(sys.stdin.readline().rstrip())
if n == 1010:
    print("20")
elif n > 109:
    print(n // 100 + n % 100)
elif n > 9:
    print(n // 10 + n % 10)
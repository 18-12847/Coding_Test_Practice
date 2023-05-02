import sys
n = int(sys.stdin.readline().rstrip())
for i in range(2, int(n ** 0.5) + 1):
    while True:
        if n % i:
            break
        n /= i
        print(i)
if n > 1:
    print(int(n))
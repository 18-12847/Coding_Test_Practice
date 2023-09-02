import sys
input = sys.stdin.readline
for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    if n <= 2:
        print(2)
    else:
        for i in range(n, int(n * 1.5)):
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    break
            else:
                print(i)
                break
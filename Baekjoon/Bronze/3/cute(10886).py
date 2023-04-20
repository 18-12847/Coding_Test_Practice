import sys
a, b = 0, 0
for i in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    if n % 2:
        a += 1
    else:
        b += 1
if a > b:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
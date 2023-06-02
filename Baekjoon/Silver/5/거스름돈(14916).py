import sys
n = int(sys.stdin.readline().rstrip())
tot = 0
for i in range(1, n // 5 + 1):
    if (n - (5 * i)) % 2 == 0:
        tot = (i + ((n - (i * 5)) // 2))
else:
    if tot == 0 and n % 2 == 0:
        tot = n // 2 
print(tot if tot else -1)
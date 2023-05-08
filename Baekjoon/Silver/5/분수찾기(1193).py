import sys
n = int(sys.stdin.readline().rstrip())
for i in range(1, 10000000):
    if i * (i + 1) / 2 <= n <= (i + 1) * (i + 2) / 2:
        num = n - int((i * (i + 1) / 2))
        break
if n == 1:
    print("1/1")
elif not(i % 2):
    print(f"{i + 2 - num}/{num}")
else:
    print(f"{num}/{i + 2 - num}")
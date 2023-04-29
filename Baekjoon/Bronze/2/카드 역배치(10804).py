import sys
lst = [i + 1 for i in range(20)]
for i in range(10):
    a, b = map(int, sys.stdin.readline().split())
    c = (b - a + 1 + (1 if (b - a + 1) % 2 else 0)) // 2
    for j in range(c):
        lst[j + a - 1], lst[b - j - 1] = lst[b - j - 1], lst[j + a - 1]
print(*lst)
import sys
a = int(sys.stdin.readline().rstrip())
b = sys.stdin.readline().rstrip()
for i in b[::-1]:
    print(a * int(i))
print(a * int(b))
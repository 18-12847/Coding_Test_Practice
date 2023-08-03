import sys
input = sys.stdin.readline
a, b = map(int, input().split())
a, b = list(map(int, input().split())), list(map(int, input().split()))
print(len(a) - len(set(a) & set(b)))
if set(a) - set(b):
    print(*sorted(set(a) - set(b)))
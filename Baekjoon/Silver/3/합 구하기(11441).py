import sys
input = sys.stdin.readline
n = int(input().rstrip())
lst = [0] + list(map(int, input().split()))
for i in range(1, n + 1):
    lst[i] += lst[i-1]
for i in range(int(input().rstrip())):
    a, b = map(int, input().split())
    print(lst[b] - lst[a-1])
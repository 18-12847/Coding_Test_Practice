import sys, math
input = sys.stdin.readline
n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(m)]
n6 = sorted(lst, key = lambda x: x[0])[0][0]
n1 = sorted(lst, key = lambda x: x[1])[0][1]
print(min((math.ceil(n / 6) * n6), min((n // 6) * n6 + ((n % 6) * n1), n1 * n)))
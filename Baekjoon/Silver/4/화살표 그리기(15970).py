#씨발 문제 존나 싸가지없네
import sys
input = sys.stdin.readline
n = int(input().rstrip())
point, color = [], []
lst = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: (x[1], x[0]))
for i in lst:
    point.append(i[0])
    color.append(i[1])
tot = 0
for i in range(n):
    if i > 0 and color[i] == color[i-1]:
        left = point[i] - point[i-1]
    else:
        left = float("inf")
    if i < n-1 and color[i] == color[i+1]:
        right = point[i+1] - point[i]
    else:
        right = float("inf")
    tot += min(left, right)
print(tot)
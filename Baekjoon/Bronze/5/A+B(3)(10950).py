a = int(input())
ans = []
for _ in range(a):
    b, c = map(int, input().split())
    ans.append(b + c)
print(*ans, sep="\n")
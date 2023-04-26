import sys
lst = [int(sys.stdin.readline().rstrip()) for _ in range(10)]
ans = [[lst.count(i), i] for i in lst]
print(int(sum(lst) / 10))
print(sorted(ans, reverse = True)[0][1])
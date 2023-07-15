import sys
n, m = map(int, sys.stdin.readline().split())
dic = {}
for i in range(n):
    s = sys.stdin.readline().rstrip()
    dic[s] = str(i+1)
    dic[str(i+1)] = s 
ans = [sys.stdin.readline().rstrip() for _ in range(m)]
for i in ans:
    print(dic[i])
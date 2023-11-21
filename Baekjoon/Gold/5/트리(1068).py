import sys
input = sys.stdin.readline

def dfs(delete):
    tree[delete] = -2
    for i in range(n):
        if delete == tree[i]:
            dfs(i)

n = int(input().rstrip())
tree = list(map(int, input().split()))
delete = int(input().rstrip())
dfs(delete)
cnt = 0
for i in range(n):
    if tree[i] != -2 and i not in tree:
        cnt += 1
print(cnt)
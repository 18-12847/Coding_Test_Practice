import sys
input = sys.stdin.readline

def rec(lst, depth):
    mid = len(lst) // 2
    tree[depth] += [lst[mid]]
    if len(lst) == 1:
        return
    rec(lst[:mid], depth + 1)
    rec(lst[mid + 1:], depth + 1)

k = int(input().rstrip())
tree = [[] for _ in range(k)]
inorder = list(map(int, input().split()))

rec(inorder, 0)
for i in tree:
    print(*i)
import sys
input = sys.stdin.readline
n = int(input().rstrip())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a] += [b]
    tree[b] += [a]
for _ in range(int(input().rstrip())):
    t, k = map(int, input().split())
    if t == 2:
        print("yes")
    elif t == 1 and len(tree[k]) > 1:
        print("yes")
    else:
        print("no")

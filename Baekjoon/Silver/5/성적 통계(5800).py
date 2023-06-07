import sys
lst = [sorted(list(map(int, sys.stdin.readline().split()))[1:]) for _ in range(int(sys.stdin.readline().rstrip()))]
for i, v in enumerate(lst):
    top = 0
    for j in range(1, len(v)):
        if top < v[j] - v[j-1]:
            top = v[j] - v[j-1]
    print(f"Class {i+1}")
    print(f"Max {max(v)}, Min {min(v)}, Largest gap {top}")
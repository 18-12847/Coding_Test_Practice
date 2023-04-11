import sys
ans = [i for i in range(1, 9)]
a = list(map(int, sys.stdin.readline().split()))
if a == ans:
    print("ascending")
elif a == list(reversed(ans)):
    print("descending")
else:
    print("mixed")
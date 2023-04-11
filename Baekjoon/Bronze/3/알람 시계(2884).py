import sys
h, m = map(int, sys.stdin.readline().split())
if h == 0 and m < 45:
    print(f"{h+23} {m+15}")
elif h > 0 and m < 45:
    print(f"{h-1} {m+15}")
else:
    print(f"{h} {m-45}")
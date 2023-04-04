import sys
n = int(sys.stdin.readline().rstrip())
cnt, tot, pt1, pt2 = 0, 0, 0, 0
while pt1 != n - 1:
    if tot < n:
        tot += pt2            
        pt2 += 1
    elif tot == n:
        cnt += 1
        tot += pt2
        pt2 += 1
    else:
        tot -= pt1
        pt1 += 1
print(cnt + 1)
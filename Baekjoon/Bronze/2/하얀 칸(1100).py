import sys
cnt = 0
for i in range(1, 9):
    for idx, val in enumerate(sys.stdin.readline().rstrip()):
        if i % 2 and idx % 2 == 0 and val == "F":
            cnt += 1
        elif i % 2 == 0 and idx % 2 and val == "F":
            cnt += 1
print(cnt)
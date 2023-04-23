import sys
lst = ["ABC2", "DEF3", "GHI4", "JKL5", "MNO6", "PQRS7", "TUV8", "WXYZ9"]
a = sys.stdin.readline().rstrip()
cnt = 0
for i in a:
    for j in range(len(lst)):
        if i in lst[j]:
            cnt += int(lst[j][-1])
print(cnt + len(a))
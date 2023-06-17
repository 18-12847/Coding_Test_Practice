import sys
s = sys.stdin.readline().rstrip()
tmp = []
for i in range(len(s) - 2):
    for j in range(i + 1, len(s) - 1):
        for k in range(j + 1, len(s)):
            ss = s[:i + 1][::-1]+s[j:k][::-1]+s[k:][::-1]
            if len(ss) == len(s):
                tmp.append(ss)
print(sorted(tmp)[0])
import sys
a = list(sys.stdin.readline().rstrip())
b = list(sys.stdin.readline().rstrip())
if a == b:
    print("0")
else:
    tmp = []
    for i in a:
        if i in b:
            tmp.append(i)
            b.remove(i)
    for j in tmp:
        a.remove(j)    
    print(len(a) + len(b))
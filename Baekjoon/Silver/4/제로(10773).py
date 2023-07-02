import sys
lst = []
for i in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    if n == 0 and lst:
        lst.pop()
    else:
        lst.append(n)
print(sum(lst))
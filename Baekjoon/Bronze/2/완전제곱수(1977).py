import sys
a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
lst = [i for i in range(a, b + 1) if i ** 0.5 == int(i ** 0.5)]
if len(lst):
    print(sum(lst), lst[0], sep = "\n")
else:
    print("-1")
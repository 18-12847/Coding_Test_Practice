import sys
s = sys.stdin.readline().rstrip()
lst = [s[i:i + 3] for i in range(0, len(s) - 2)]
print(lst.count("JOI"), lst.count("IOI"), sep = "\n")
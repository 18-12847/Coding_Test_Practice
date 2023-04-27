import sys
a, b = sys.stdin.readline().split()
a_tmp, b_tmp = a, b
a = a.replace("5", "6")
b = b.replace("5", "6")
a_tmp = a_tmp.replace("6", "5")
b_tmp = b_tmp.replace("6", "5")
print(int(a_tmp) + int(b_tmp), int(a) + int(b))
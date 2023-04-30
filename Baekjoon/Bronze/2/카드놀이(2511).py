import sys
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
lst = []
for i in range(10):
    if a[i] > b[i]:
        lst.append("a")
    elif a[i] == b[i]:
        lst.append("d")
    else:
        lst.append("b")
a_tot, b_tot = lst.count("a") * 3 + lst.count("d"), lst.count("b") * 3 + lst.count("d")
lst = "".join(lst).replace("d","")
print(a_tot, b_tot)
if a_tot > b_tot:
    print("A")
elif a_tot < b_tot:
    print("B")
elif a_tot == b_tot and not lst:
    print("D")
else:
    print(lst[-1].upper())
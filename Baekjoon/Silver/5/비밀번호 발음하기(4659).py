import sys
from itertools import permutations
lst = []
while True:
    s = sys.stdin.readline().rstrip()
    if s == "end":
        break
    lst.append(s)
for i in lst:
    flag1, flag21, flag22, flag3 = True, True, True, True
    dic = set(i)
    if ("a" in i) or ("e" in i) or ("i" in i) or ("o" in i) or ("u" in i):
        flag1 = True
    else:
        flag1 = False
    tmp1 = list(permutations(list("aeiou"), 3))
    tmp2 = list(permutations(list("bcdfghjklmnpqrstvwxyz"), 3))
    for j in tmp1:
        if "".join(j) in i:
            flag21 = False
            break
    else:
        flag21 = True
    for j in tmp2:
        if "".join(j) in i:
            flag22 = False
            break
    else:
        flag22 = True
    for k in dic:
        if k * 2 in i:
            if k * 2 in ["ee", "oo"]:
                flag3 = True
            else:
                flag3 = False
    if flag1 and flag21 and flag22 and flag3:
        print(f"<{i}> is acceptable.")
    else:
        print(f"<{i}> is not acceptable.")
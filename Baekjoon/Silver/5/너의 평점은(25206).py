import sys
lst = [sys.stdin.readline().split() for _ in range(20)]
dic = {"A+" : 4.5, "A0": 4.0, "B+" : 3.5, "B0" : 3.0, "C+" : 2.5, "C0" : 2.0, "D+" : 1.5, "D0" : 1.0, "F" : 0.0}
tot, cnt = 0, 0
for i in lst:
    if i[2] != "P":
        cnt += float(i[1])
        tot += dic[i[2]] * float(i[1])
print("{:.6f}".format(tot / cnt))
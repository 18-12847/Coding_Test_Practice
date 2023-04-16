import sys
n = int(sys.stdin.readline().rstrip())
dic = {1:1, 2:2, 3:3, 4:4, 5:5, 6:4, 7:3, 8:2}
if n >= 8 and n % 8 == 0:
    print(dic[(n + 2) % 8])
elif n >= 8:
    print(dic[(n - 8) % 8])
else:
    print(dic[n % 8])
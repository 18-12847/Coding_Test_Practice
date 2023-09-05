import sys
input = sys.stdin.readline
dic = {}
for i in range(int(input().rstrip())):
    inp = list(map(int, input().split()))
    if inp[0] == 1:
        dic[inp[2]] = inp[1]
    else:
        print(dic[inp[1]])
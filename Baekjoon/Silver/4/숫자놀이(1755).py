import sys, math
input = sys.stdin.readline
n, m = map(int, input().split())
dic = {0 : "zero", 1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", 7 : "seven", 8 : "eight", 9 : "nine"}
ans = []
for i in range(n, m + 1):
    s = ""
    for j in list(str(i)):
        s += dic[int(j)]
    ans.append(s)
cnt = 0
for i in sorted(ans):
    print(i.replace("one", "1").replace("two", "2").replace("three", "3").replace("four", "4").replace("five", "5").replace("six", "6").replace("seven", "7").replace("eight", "8").replace("nine", "9").replace("zero", "0"), end = " ")
    cnt += 1
    if cnt == 10:
        print()
        cnt = 0
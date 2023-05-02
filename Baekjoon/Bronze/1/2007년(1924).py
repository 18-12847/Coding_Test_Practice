import sys
x, y = map(int, sys.stdin.readline().split())
dict = {1 : 0, 2 : 31, 3 : 59, 4 : 90, 5 : 120, 6 : 151, 7 : 181, 8 : 212, 9 : 243, 10 : 273, 11 : 304, 12 : 334}
ans = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
print(ans[(dict[x] + y) % 7])
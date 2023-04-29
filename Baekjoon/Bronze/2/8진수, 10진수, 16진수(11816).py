import sys
x = sys.stdin.readline().rstrip()
if x[:2] == "0x":
    print(int(x, 16))
elif str(int(x)) == x:
    print(int(x))
else:
    print(int(x, 8))
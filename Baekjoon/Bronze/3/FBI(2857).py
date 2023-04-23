import sys
cnt = 0
for i in range(5):
    if "FBI" in sys.stdin.readline().rstrip():
        print(i + 1, end = " ")
        cnt += 1
if not cnt:
    print("HE GOT AWAY!")
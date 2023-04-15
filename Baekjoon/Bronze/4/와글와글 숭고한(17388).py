import sys
s, k, h = map(int, sys.stdin.readline().split())
if s + k + h > 99:
    print("OK")
elif s < k and s < h:
    print("Soongsil")
elif k < s and k < h:
    print("Korea")
elif h < s and h < k:
    print("Hanyang")
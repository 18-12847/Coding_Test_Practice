import sys
def recursion(s, l, r, cnt):
    if l >= r:
        return 1, cnt
    elif s[l] != s[r]:
        return 0, cnt
    else:
        return recursion(s, l + 1, r - 1, cnt + 1)

def isPalindrome(s):
    result, cnt = recursion(s, 0, len(s) - 1, 1)
    return result, cnt

for i in range(int(sys.stdin.readline().rstrip())):
    s = sys.stdin.readline().rstrip()
    result, cnt = isPalindrome(s)
    print(result, cnt)
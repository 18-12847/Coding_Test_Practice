import sys
n = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()
ans = []
for i in s:
    if (i == "S" and ans and ans[-1] == "*") or (i == "L" and ans and ans[-1] == "*"):
        ans.append(i)
    elif i == "L" and ans and ans[-1] == "L":
        ans.append(i)
        ans.append("*")
    else:
        ans.append("*")
        ans.append(i)
if s[-1] == "S":
    ans.append("*")
print(min(ans.count("*"), n))
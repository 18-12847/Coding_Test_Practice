import sys
from collections import deque
lst = deque()
for i in range(int(sys.stdin.readline().rstrip())):
    s = sys.stdin.readline().split()
    if len(s) == 2:
        if s[0] == "push_front":
            lst.appendleft(s[1])
        else:
            lst.append(s[1])
    else:
        if s == ["pop_front"]:
            print(lst.popleft() if lst else -1)
        elif s == ["pop_back"]:
            print(lst.pop() if lst else -1)
        elif s == ["size"]:
            print(len(lst))
        elif s == ["empty"]:
            print(0 if lst else 1)
        elif s == ["front"]:
            print(lst[0] if lst else -1)
        else:
            print(lst[-1] if lst else -1)
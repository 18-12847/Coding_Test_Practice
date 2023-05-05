import sys
lst = [int(sys.stdin.readline().rstrip()) for i in range(int(sys.stdin.readline().rstrip()))]
for i in lst:
    flag = False
    ans = [int(j * (j + 1) / 2) for j in range(1, int(i ** 0.7) + 1)]
    for a in ans:
        if flag:
            break
        for b in ans:
            if flag:
                break
            for c in ans:
                if flag:
                    break
                if a + b + c == i:
                    print("1")
                    flag = True
                    break
    else:
        print("0")
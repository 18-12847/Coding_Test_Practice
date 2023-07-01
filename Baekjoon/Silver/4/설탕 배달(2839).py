import sys
n = int(sys.stdin.readline().rstrip())
n1 = n
for i in range(n // 5, 0, -1):
    tot = 0
    tot += i
    if (n - (i * 5)) % 3 == 0:
        tot += (n - (i * 5)) // 3
        print(tot)
        break
else:
    for j in range(n1 // 3, 0, -1):
        tot1 = 0
        tot1 += j
        if (n1 - (j * 3)) % 5 == 0:
            tot1 += (n1 - (j * 3)) // 5
            print(tot1)
            break
    else:
        print(-1)
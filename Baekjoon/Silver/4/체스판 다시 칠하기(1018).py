import sys
n, m = map(int, sys.stdin.readline().split())
lst = list(sys.stdin.readline().rstrip() for i in range(n))
zero1, one1 = "WBWBWBWB", "BWBWBWBW"
zero2, one2 = "BWBWBWBW", "WBWBWBWB"
ans = []
for i in range(n - 7):
    for j in range(m - 7):
        tot1 = tot2 = 0
        for k in range(8):
            tmp = lst[i+k][j:j+8]
            for a in range(8):
                if k % 2 == 0:
                    if tmp[a] != zero1[a]:
                        tot1 += 1
                    if tmp[a] != zero2[a]:
                        tot2 += 1
                else:
                    if tmp[a] != one1[a]:
                        tot1 += 1
                    if tmp[a] != one2[a]:
                        tot2 += 1
        ans.append(min(tot1, tot2))
print(min(ans))
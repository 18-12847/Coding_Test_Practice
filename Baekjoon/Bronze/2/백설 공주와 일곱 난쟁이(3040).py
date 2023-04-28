import sys
lst = [int(sys.stdin.readline().rstrip()) for _ in range(9)]
for a in range(0, 3):
    for b in range(a + 1, 4):
        for c in range(b + 1, 5):
            for d in range(c + 1, 6):
                for e in range(d + 1, 7):
                    for f in range(e + 1, 8):
                        for g in range(f + 1, 9):
                            if lst[a] + lst[b] + lst[c] + lst[d] + lst[e] + lst[f] + lst[g] == 100:
                                ans = [lst[a], lst[b], lst[c], lst[d], lst[e], lst[f], lst[g]]
print(*ans, sep = "\n")
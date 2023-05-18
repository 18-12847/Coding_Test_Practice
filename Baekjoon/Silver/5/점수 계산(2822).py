import sys
lst = [int(sys.stdin.readline().rstrip()) for _ in range(8)]
for a in range(4):
    for b in range(a + 1, 5):
        for c in range(b + 1, 6):
            for d in range(c + 1, 7):
                for e in range(d + 1, 8):
                    if sorted([lst[a], lst[b], lst[c], lst[d], lst[e]], reverse = True) == sorted(lst, reverse = True)[:5]:
                        print(sum([lst[a], lst[b], lst[c], lst[d], lst[e]]))
                        print(a + 1, b + 1, c + 1, d + 1, e + 1)
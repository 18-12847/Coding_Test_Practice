import sys
for i in range(int(sys.stdin.readline().rstrip())):
    a, b = sys.stdin.readline().split()
    a, b = list(a), list(b)
    print("Distances: ", end = "")
    for i in zip(a, b):
        if ord(i[0]) > ord(i[1]):
            print(ord(i[1]) + 26 - ord(i[0]), end =" ")
        else:
            print(abs(ord(i[0]) - ord(i[1])), end =" ")
    print()
import sys
input = sys.stdin.readline
n = int(input().rstrip())
inp = list(map(int, input().split()))
for _ in range(int(input().rstrip())):
    a, b = map(int, input().split())
    if a == 1:
        for i in range(b-1, n, b):
            inp[i] = abs(inp[i]-1)
    else:
        cnt = 0
        if len(inp[:b-1]) < len(inp[b:]):
            for i in range(b-2, -1, -1):
                if inp[i] == inp[b+(b-i)-2]:
                    cnt += 1
                else:
                    break
            if not cnt:
                inp[b-1] = abs(inp[b-1]-1)
            else:
                for i in range(cnt):
                    inp[b-i-2] = abs(inp[b-i-2]-1)
                    inp[b+i] = abs(inp[b+i]-1)
                inp[b-1] = abs(inp[b-1]-1)
        else:
            for i in range(b, n):
                if inp[i] == inp[b-(i-b)-2]:
                    cnt += 1
                else:
                    break
            if not cnt:
                inp[b-1] = abs(inp[b-1]-1)
            else:
                for i in range(cnt):
                    inp[b-i-2] = abs(inp[b-i-2]-1)
                    inp[b+i] = abs(inp[b+i]-1)
                inp[b-1] = abs(inp[b-1]-1)
cnt = 0
for i in inp:
    print(i, end = " ")
    cnt += 1
    if cnt % 20 == 0:
        print()
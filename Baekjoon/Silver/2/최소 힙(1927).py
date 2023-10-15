import sys, heapq
input = sys.stdin.readline
heap = []
for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    if not n:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, n)
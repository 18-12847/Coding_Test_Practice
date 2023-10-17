import heapq, sys
input = sys.stdin.readline
heap = []
for _ in range(int(input().rstrip())):
    x = int(input().rstrip())
    if x:
        heapq.heappush(heap, (-x, x))
    else:
        print(heapq.heappop(heap)[1] if heap else 0)
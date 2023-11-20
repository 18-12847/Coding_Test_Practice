import sys, heapq
input = sys.stdin.readline
heap = []
for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    if heap and not n:
        print(heapq.heappop(heap)[1])
    elif not heap and not n:
        print(0)
    elif n:
        heapq.heappush(heap, (abs(n), n))
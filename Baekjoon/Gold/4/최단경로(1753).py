import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        cur_dist, cur_loc = heapq.heappop(heap)
        if distance[cur_loc] < cur_dist:
            continue
        for next_loc, next_dist in graph[cur_loc]:
            cost = cur_dist + next_dist
            if distance[next_loc] > cost:
                distance[next_loc] = cost
                heapq.heappush(heap, (cost, next_loc))

n, m = map(int, input().split())
s = int(input().rstrip())
graph = [[] for _ in range(n + 1)]
distance = [float("inf") for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a] += [(b, c)]

dijkstra(s)
for i in distance[1:]:
    print("INF" if i == float("inf") else i)
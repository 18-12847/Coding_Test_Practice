import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        cur_dist, cur_city = heapq.heappop(heap)
        if distance[cur_city] < cur_dist:
            continue
        for i in graph[cur_city]:
            next_city, next_dist = i[0], i[1]
            cost = cur_dist + next_dist
            if cost < distance[next_city]:
                distance[next_city] = cost
                heapq.heappush(heap, (cost, next_city))

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [float("inf")] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a] += [(b, c)]
    graph[b] += [(a, c)]

dijkstra(1)
print(distance[-1])
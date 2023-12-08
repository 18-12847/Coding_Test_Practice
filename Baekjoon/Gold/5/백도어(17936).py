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
            if distance[next_loc] > cost and not ward[next_loc]:
                distance[next_loc] = cost
                heapq.heappush(heap, (cost, next_loc))
    return distance[-1]

n, m = map(int, input().split())
ward = list(map(int, input().split()))
ward[-1] = 0
graph = [[] for _ in range(n)]
distance = [float("inf") for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a] += [(b, c)]
    graph[b] += [(a, c)]

ans = dijkstra(0)
print(-1 if ans == float("inf") else ans)
import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start)) #거리 0과 시작 도시 추가(거리 기준으로 힙을 구성해야함)
    distance[start] = 0 #시작 도시 거리는 0
    while heap:
        cur_dist, cur_city = heapq.heappop(heap) #현재 도시까지 거리와 현재 도시 추출
        if distance[cur_city] < cur_dist: #현재 도시까지 알려진 최단거리보다 현재 거리가 크면
            continue # 무시하고 다시 heappop
        for next_city, next_dist in graph[cur_city]: #현재 도시에서 갈 수 있는 도시 탐색
            cost = cur_dist + next_dist #현재 도시에서 다음 도시까지 거리 합
            if cost < distance[next_city]: #만약 비용이 다음 도시 거리보다 작으면
                distance[next_city] = cost #다음 도시 거리를 현재 비용으로 업데이트
                heapq.heappush(heap, (cost, next_city)) #새로 계산된 거리와 다음 도시 추가

city = int(input().rstrip())
bus = int(input().rstrip())
graph = [[] for _ in range(city + 1)]
distance = [float("inf")] * (city + 1)
for _ in range(bus):
    a, b, c = map(int, input().split())
    graph[a] += [(b, c)] #a정점에서 b정점까지 c만큼 거리

start, end = map(int, input().split())
dijkstra(start)
print(distance[end])
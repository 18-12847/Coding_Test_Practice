import sys, heapq
input = sys.stdin.readline

def prim(graph, visited, tot):
    heap, mst = [], 0
    heapq.heappush(heap, (0, 0))
    while heap:
        c_dist, c_node = heapq.heappop(heap)
        if not visited[c_node]:
            visited[c_node] = 1
            mst += c_dist
        else:
            continue
        for n_node, n_dist in graph[c_node]:
            if visited[n_node]:
                continue
            heapq.heappush(heap, (n_dist, n_node))
    print(tot - mst)

def solve():
    while True:
        tot = 0
        m, n = map(int, input().split())
        if (m, n) == (0, 0):
            exit()
        graph = [[] for _ in range(m)]
        visited = [0] * (m)
        for _ in range(n):
            a, b, c = map(int, input().split())
            tot += c
            graph[a].append((b, c))
            graph[b].append((a, c))
        prim(graph, visited, tot)

solve()
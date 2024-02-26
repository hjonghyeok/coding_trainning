import sys, heapq
import copy
n, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
v1, v2 = map(int, sys.stdin.readline().split())

def dijkstra(s, graph, n):
    q = []
    distance = [float('inf')] * (n+1)
    distance[s] = 0
    heapq.heappush(q, (0, s))
    while q:
        cost, node = heapq.heappop(q)
        if cost > distance[node]:
            continue
        for i in graph[node]:
            n_cost = cost+i[1]
            if n_cost < distance[i[0]]:
                distance[i[0]] = n_cost
                heapq.heappush(q, (n_cost, i[0]))
    return distance

dist_1 = dijkstra(1, graph, n)
dist_v1 = dijkstra(v1, graph, n)
dist_v2 = dijkstra(v2, graph, n)

path_1 = dist_1[v1] + dist_v1[v2] + dist_v2[n]
path_2 = dist_1[v2] + dist_v2[v1] + dist_v1[n]

answer = min(path_1, path_2)
if answer == float('inf'):
    print(-1)
else:
    print(answer)

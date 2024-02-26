import sys, heapq

n, m, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
r_graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))
    r_graph[b].append((a,c))

def fn(start, graph, n):
    distance = [float('inf')] *(n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, node = heapq.heappop(q)
        if dist > distance[node]:
            continue
        for i in graph[node]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

from_x = fn(x, graph, n)
to_x = fn(x, r_graph, n)

answer = 0
for i in range(1, n+1):
    answer = max(answer, from_x[i]+to_x[i])
print(answer)
    

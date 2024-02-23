import sys
import heapq

input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

s, e = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance = [float('inf')] * (n+1)
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for cost, next_node in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(q, (new_cost, next_node))
    return distance[e]

print(dijkstra(s))
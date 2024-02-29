import heapq

n = int(input())
q = []
for _ in range(n):
    heapq.heappush(q, int(input()))

while q:
    print(heapq.heappop(q))

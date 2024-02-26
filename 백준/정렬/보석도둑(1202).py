import sys, heapq

n, k = map(int, sys.stdin.readline().split())
q = []
for _ in range(n):
    m, v = map(int, sys.stdin.readline().split())
    heapq.heappush(q, (m, -v))

bag = sorted([int(sys.stdin.readline()) for _ in range(k)])

arr = []
answer = 0
for i in bag:
    while q and q[0][0] <= i:
        m, v = heapq.heappop(q)
        heapq.heappush(arr, v)
    
    if arr:
        answer += -heapq.heappop(arr)

print(answer)
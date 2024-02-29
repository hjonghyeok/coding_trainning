import sys, heapq

n, k = map(int, sys.stdin.readline().split())
arr = [0] * (max(n, k) * 2 + 1)

q = []
heapq.heappush(q, (0, n))
arr[n] = 1
while q:
    cost, x = heapq.heappop(q)
    if x == k:
        print(cost)
        break
    if len(arr) > x*2 and not arr[x*2]:
        arr[x*2] = 1
        heapq.heappush(q, (cost, x*2))
    for i in [x+1, x-1]:
        if 0 <= i < len(arr) and not arr[i]:
            arr[i] = 1
            heapq.heappush(q, (cost + 1, i))
            
        

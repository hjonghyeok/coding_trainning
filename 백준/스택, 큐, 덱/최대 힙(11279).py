import sys, heapq

n = int(sys.stdin.readline().strip())
q = []

for _ in range(n):
    x = int(sys.stdin.readline().strip())
    if x != 0:
        heapq.heappush(q, (-x, x))
    else:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q)[1])
            

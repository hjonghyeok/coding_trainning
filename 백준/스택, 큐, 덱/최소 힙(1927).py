import sys, heapq

q = []

for _ in range(int(sys.stdin.readline().strip())):
    x = int(sys.stdin.readline().strip())
    if x != 0:
        heapq.heappush(q, x)
    else:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q))

import sys, heapq

for _ in range(int(sys.stdin.readline())):
    max_q, min_q = [], []
    visited = [0] * 1000001
    
    for i in range(int(sys.stdin.readline())):
        cmd, n = sys.stdin.readline().split()
        n = int(n)
        if cmd == 'I':
            heapq.heappush(max_q, (-n, i))
            heapq.heappush(min_q, (n, i))
            visited[i] = 1
        else:
            if n == 1:
                while max_q and not visited[max_q[0][1]]:
                    heapq.heappop(max_q)
                if max_q:
                    visited[max_q[0][1]] = 0
                    heapq.heappop(max_q)
            else:
                while min_q and not visited[min_q[0][1]]:
                    heapq.heappop(min_q)
                if min_q:
                    visited[min_q[0][1]] = 0
                    heapq.heappop(min_q)
                
    while min_q and not visited[min_q[0][1]]:
        heapq.heappop(min_q)
    while max_q and not visited[max_q[0][1]]:
        heapq.heappop(max_q)
        
    if min_q and max_q:
        print(-max_q[0][0], min_q[0][0])
    else:
        print("EMPTY")
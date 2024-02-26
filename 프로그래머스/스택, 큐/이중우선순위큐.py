import heapq

def solution(operations):
    max_q = []
    min_q = []
    visited = []
    idx = 0
    for i in operations:
        cmd, value = i.split()
        if cmd == "I":
            heapq.heappush(max_q, (-int(value), idx))
            heapq.heappush(min_q, (int(value), idx))
            visited.append(0)
            idx += 1
        else:
            if max_q and min_q:
                if value == "1":
                    while max_q and visited[max_q[0][1]]:
                        heapq.heappop(max_q)
                    if max_q:
                        
                        visited[heapq.heappop(max_q)[1]] = 1
                else:
                    while min_q and visited[min_q[0][1]]:
                        heapq.heappop(min_q)
                    if min_q:
                        visited[heapq.heappop(min_q)[1]] = 1
                
    while max_q and visited[max_q[0][1]]:
        heapq.heappop(max_q)              
    while min_q and visited[min_q[0][1]]:
        heapq.heappop(min_q)              
    
    if max_q and min_q:
        return [-max_q[0][0], min_q[0][0]]
    else:
        return [0,0]


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
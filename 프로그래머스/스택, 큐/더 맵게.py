import heapq

def solution(scoville, K):
    q = []
    answer = 0
    for i in scoville:
        heapq.heappush(q, i)
    while q[0] < K:
        a = heapq.heappop()
        b = heapq.heappop()
        heapq.heappush(q, a + b*2)
        answer += 1
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))
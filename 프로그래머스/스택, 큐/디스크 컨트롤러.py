import heapq

def solution(jobs):
    jobs.sort()
    time, end, count = 0, 0, 0
    wait = []
    total_length = len(jobs)
    answer = []
    visited = [0] * total_length
    while count < total_length:
        for job in range(total_length):
            if end <= jobs[job][0] <= time and not visited[job]:
                heapq.heappush(wait, (jobs[job][1], jobs[job][0]))
                visited[job] = 1
        if wait:
            current = heapq.heappop(wait)
            end = time
            time += current[0]
            count += 1
            answer.append(time - current[1])
        else:
            time += 1
    return sum(answer) // len(answer)

print(solution([[0, 3], [1, 9], [2, 6]]))
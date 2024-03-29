from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if not visited[i]:
            answer += 1
            q = deque()
            q.append(i)
            visited[i] = 1
            while q:
                node = q.popleft()
                for j in range(n):
                    if not visited[j] and computers[node][j]:
                        q.append(j)
                        visited[j] = 1
    
                    
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
print(solution(3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
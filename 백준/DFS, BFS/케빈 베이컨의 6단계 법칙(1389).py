import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())
graph = [[False] * (n+1) for _ in range(n+1)] 
for _ in range(1, m+1):
    a = list(map(int, sys.stdin.readline().strip().split()))
    graph[a[0]][a[1]] = True
    graph[a[1]][a[0]] = True
    
result = []
for i in range(1, n+1):
    visited = [-1] * (n+1)
    visited[i] = 0
    q = deque([i])
    while q:
        node = q.popleft()
        for j in range(1, n+1):
            if visited[j] == -1 and graph[node][j]:
                q.append(j)
                visited[j] = visited[node] + 1
    result.append(sum(visited)+1)

answer = 0
for i in range(1, len(result)):
    if result[answer] > result[i]:
        answer = i
print(answer+1)


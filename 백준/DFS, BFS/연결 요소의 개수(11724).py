import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())

graph = [[0] * (n+1) for _ in range(n+1)]

visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        cnt += 1
        q = deque()
        q.append(i)
        visited[i] = 1
        while q:
            node = q.popleft()
            for j in range(i, n+1):
                if (not visited[j]) and graph[node][j]:
                    q.append(j)
                    visited[j] = 1

print(cnt)
            
        
import sys
from collections import deque

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

graph = [[False] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a][b] = True
    graph[b][a] = True
    
visited = [0] * (n+1)

q = deque([1])
visited[1] = 1
while q:
    node = q.popleft()
    for i in range(1, n+1):
        if not visited[i] and graph[node][i]:
            q.append(i)
            visited[i] = 1

print(sum(visited)-1)
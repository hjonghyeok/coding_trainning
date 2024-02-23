import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

for i in range(n):
    q = deque()
    q.append(i)
    while q:
        node = q.popleft()
        for j in range(n):
            if graph[node][j] and not visited[i][j]:
                q.append(j)
                visited[i][j] = 1
                
for i in visited:
    for j in i:
        print(j, end=" ")
    print()

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(n)]

q = deque()
q.append((0, 0))
graph[0][0] = 1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (0 <= nx < n) and (0 <= ny < m) and (graph[nx][ny] == '1'):
            q.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1
            
print(graph[n-1][m-1])
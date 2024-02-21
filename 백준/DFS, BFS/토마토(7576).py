import sys
from collections import deque

m, n = map(int, sys.stdin.readline().strip().split())
tomatos = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

q = deque()
for i in range(n):
    for j in range(m):
        if tomatos[i][j] == 1:
            q.append((i, j))
            visited[i][j] = 1

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (0 <= nx < n) and (0 <= ny < m) and (not visited[nx][ny]) and (tomatos[nx][ny] == 0):
            q.append((nx,ny))
            tomatos[nx][ny] = tomatos[x][y] + 1
            visited[nx][ny] = 1

answer = 1
for i in tomatos:
    if not answer:
        break
    for j in i:
        if j == 0:
            answer = 0
            break
        elif j > answer:
            answer = j
print(answer - 1)
import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().strip().split())

tomatos = []
q = deque()

for i in range(h):
    L = []
    for j in range(n):
        a = list(map(int, sys.stdin.readline().strip().split()))
        L.append(a)
        for k in range(len(a)):
            if a[k] == 1:
                q.append((i, j, k))
    tomatos.append(L)

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while q:
    x, y, z = q.popleft()
    for i in range(6):
        nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
        if (0 <= nx < h) and (0 <= ny < n) and (0 <= nz < m) and (not tomatos[nx][ny][nz]):
            q.append((nx,ny,nz))
            tomatos[nx][ny][nz] = tomatos[x][y][z] + 1

answer = 0
iszero = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomatos[i][j][k] == 0:
                iszero = 1
            if tomatos[i][j][k] > answer:
                answer = tomatos[i][j][k]

if iszero:
    print(-1)
else:
    print(answer-1)
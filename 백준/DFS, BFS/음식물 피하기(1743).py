import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
maps = [[0]*m for _ in range(n)]
tresh = []
for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    tresh.append((x-1, y-1))
    maps[x-1][y-1] = 1

answer = 0
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
for i, j in tresh:
    q = deque()
    q.append((i, j))
    cnt = 1
    maps[i][j] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0<= nx < n) and (0<= ny < m) and maps[nx][ny]:
                cnt += 1
                q.append((nx, ny))
                maps[nx][ny] = 0
    answer = max(answer, cnt)
print(answer)
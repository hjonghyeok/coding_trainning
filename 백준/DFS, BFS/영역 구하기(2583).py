import sys
from collections import deque

m, n, k = map(int, sys.stdin.readline().split())
maps = [[0] * (n) for _ in range(m)]
a = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]

for x1, y1, x2, y2 in a:
    for i in range(y1, y2):
        for j in range(x1, x2):
            maps[i][j] = 1

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

answer = []
for i in range(m):
    for j in range(n):
        if not maps[i][j]:
            cnt = 1
            q = deque()
            q.append((i, j))
            maps[i][j] = 1
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0<= nx < m and 0<= ny < n and not maps[nx][ny]:
                        q.append((nx, ny))
                        maps[nx][ny] = 1
                        cnt += 1
            answer.append(cnt)
answer.sort()
print(len(answer))
for i in answer:
    print(i, end=" ")
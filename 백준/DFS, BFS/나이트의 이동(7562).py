import sys
from collections import deque


dx = [1, 1, -1, -1, 2, -2, 2, -2]
dy = [2, -2, 2, -2, 1, 1, -1, -1]

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    maps = [[0] * n for _ in range(n)]
    x_s, y_s = map(int, sys.stdin.readline().split())
    x_e, y_e = map(int, sys.stdin.readline().split())
    q = deque()
    q.append((x_s, y_s))
    maps[x_s][y_s] = 1
    while q:
        x, y = q.popleft()
        if x == x_e and y == y_e:
            break
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and not maps[nx][ny]:
                q.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1
    
    print(maps[x_e][y_e]-1)
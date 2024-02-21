import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().strip()) for _ in range(n)]

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

cnt = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            count = 1
            q = deque()
            q.append((i, j))
            graph[i][j] = 0
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if (0 <= nx < n) and (0 <= ny < n) and (graph[nx][ny] == '1'):
                        count += 1
                        q.append((nx,ny))
                        graph[nx][ny] = 0
            cnt.append(count)

print(len(cnt))
cnt.sort()
for i in cnt:
    print(i)
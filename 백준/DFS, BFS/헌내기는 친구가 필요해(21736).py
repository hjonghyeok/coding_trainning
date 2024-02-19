import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())
campus = []
visited = [[0] * m for _ in range(n)]
x, y = 0, 0
for _ in range(n):
    a = list(sys.stdin.readline().strip())
    if 'I' in a:
        x = _
        y = a.index('I')
    campus.append(a)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
q.append((x, y))
visited[x][y] = 1
cnt = 0
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and campus[nx][ny] != 'X':
            if not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))
                if campus[nx][ny] == 'P':
                    cnt += 1

if cnt:
    print(cnt)    
else:
    print("TT")

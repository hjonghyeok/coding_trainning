import sys
from collections import deque

t = int(sys.stdin.readline().strip())

def bfs(grounds, x, y, n, m):
    q = deque()
    q.append((x, y))
    grounds[x][y] = 0
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m) and (grounds[nx][ny]):
                q.append((nx, ny))
                grounds[nx][ny] = 0
        
        

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().strip().split())
    grounds = [[0] * m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, sys.stdin.readline().strip().split())
        grounds[x][y] = 1
    
    cnt = 0
    
    for i in range(n):
        for j in range(m):
            if grounds[i][j] == 1:
                cnt += 1
                bfs(grounds, i, j, n, m)
                
    print(cnt)
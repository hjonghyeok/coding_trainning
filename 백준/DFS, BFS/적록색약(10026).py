import sys
from collections import deque

n = int(sys.stdin.readline().strip())
draw = []
for _ in range(n):
    draw.append(list(sys.stdin.readline().strip()))
    
cnt = 0
for i in range(n):
    for j in range(n):
        if draw[i][j] not in [1, 2]:
            cnt += 1
            target = draw[i][j]
            q = deque()
            x, y = i, j
            q.append((x, y))
            if draw[x][y] in 'RG':
                draw[x][y] = 1
            elif draw[x][y] == 'B':
                draw[x][y] = 2
            
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]
            
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if (0 <= nx < n) and (0 <= ny < n) and (draw[nx][ny] == target):
                        q.append((nx, ny))
                        if draw[nx][ny] in 'RG':
                            draw[nx][ny] = 1
                        elif draw[nx][ny] == 'B':
                            draw[nx][ny] = 2
                    
print(cnt, end=" ")
cnt = 0
for i in range(n):
    for j in range(n):
        if draw[i][j]:
            cnt += 1
            target = draw[i][j]
            q = deque()
            x, y = i, j
            q.append((x, y))
            draw[x][y] = 0
            
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]
            
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if (0 <= nx < n) and (0 <= ny < n) and (draw[nx][ny] == target):
                        q.append((nx, ny))
                        draw[nx][ny] = 0

print(cnt)
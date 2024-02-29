import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

q = deque()
answer = 0
answer2 = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for i in range(n):
    for j in range(m):
        if not arr[i][j]:
            continue
        else:
            answer2 += 1
            cnt = 1
            q.append((i, j))
            arr[i][j] = 0
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if (0<=nx<n) and (0<=ny<m) and arr[nx][ny]:
                        q.append((nx, ny))
                        arr[nx][ny] = 0
                        cnt += 1
            answer = max(cnt, answer)
print(answer2)            
print(answer)

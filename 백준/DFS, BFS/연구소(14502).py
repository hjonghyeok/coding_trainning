import sys
from collections import deque
import copy

n, m = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

result = 0

def bfs():
    global result
    q = deque()
    map2 = copy.deepcopy(maps)
    for i in range(n):
        for j in range(m):
            if map2[i][j] == 2:
                q.append((i, j))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if (0<=nx<n) and (0<=ny<m) and not map2[nx][ny]:
                q.append((nx, ny))
                map2[nx][ny] = 2

    count = 0
    for i in map2:
        for j in i:
            if not j:
                count += 1
    
    result = max(count, result)

def dfs(count):
    if count == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if not maps[i][j]:
                maps[i][j] = 1
                dfs(count + 1)
                maps[i][j] = 0
                
dfs(0)                
print(result)
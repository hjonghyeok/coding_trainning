import sys
from collections import deque

n, m = map(int, input().split()) # 입력 받는 부분을 sys.stdin.readline() 대신 input()으로 변경 가능
maps = [list(map(int, input().split())) for _ in range(n)] # 동일한 변경 적용
year = 0
dx, dy = [0,0,1,-1], [1, -1, 0, 0]

def melt(): # 빙산 녹이는 함수
    melting = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] > 0:
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 0:
                        melting[i][j] += 1
    for i in range(n):
        for j in range(m):
            maps[i][j] = max(0, maps[i][j] - melting[i][j])

def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] > 0:
                visited[nx][ny] = True
                q.append((nx, ny))

while True:
    cnt = 0
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] > 0 and not visited[i][j]:
                bfs(i, j, visited)
                cnt += 1
    if cnt >= 2:
        print(year)
        break
    elif cnt == 0:
        print(0)
        break
    melt()
    year += 1
import sys
from collections import deque

dx = [0,0,0,0,1,-1]
dy = [0,0,1,-1,0,0]
dz = [1,-1,0,0,0,0]


while 1:
    l, r, c = map(int, sys.stdin.readline().split())
    if not l and not r and not c:
        break
    maps = []
    for _ in range(l):
        maps.append([list(sys.stdin.readline().rstrip()) for _ in range(r)])
        input()
    x_s, y_s, z_s = 0,0,0
    x_e, y_e, z_e = 0,0,0
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if maps[i][j][k] == 'S':
                    x_s, y_s, z_s = i, j, k
                elif maps[i][j][k] == 'E':
                    x_e, y_e, z_e = i, j, k
    q = deque()
    q.append((x_s, y_s, z_s))
    maps[x_s][y_s][z_s] = 0
    while q:
        x, y, z = q.popleft()
        if x == x_e and y == y_e and z == z_e:
            break    
        for i in range(6):
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
            if 0 <= nx < l and 0 <= ny < r and 0 <= nz< c and (maps[nx][ny][nz] == '.' or maps[nx][ny][nz] == 'E'):
                q.append((nx, ny, nz))
                maps[nx][ny][nz] = maps[x][y][z] + 1
            
    if maps[x_e][y_e][z_e] == 'E':
        print('Trapped!')
    else:
        print(f'Escaped in {maps[x_e][y_e][z_e]} minute(s).')
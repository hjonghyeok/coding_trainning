import sys
from collections import deque
n = int(sys.stdin.readline())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = [1]
min_v, max_v = min(map(min, maps)), max(map(max, maps))

dx, dy = [0,0,1,-1], [1,-1,0,0]


for i in range(min_v, max_v):
    cnt = 0
    visited = [[0]*(n) for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if maps[j][k] > i and not visited[j][k]:
                cnt += 1
                q = deque()
                q.append((j, k))
                visited[j][k] = 1
                while q:
                    x, y = q.popleft()
                    for l in range(4):
                        nx, ny = x+dx[l], y+dy[l]
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and maps[nx][ny] > i:
                            q.append((nx, ny))
                            visited[nx][ny] = 1
    answer.append(cnt)
print(max(answer))
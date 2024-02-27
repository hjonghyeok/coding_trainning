import sys
from collections import deque

def dfs(node):
    visited1[node] = True
    
    print(node, end=" ")
    
    for i in range(1, n+1):
        if not visited1[i] and graph[node][i]:
            dfs(i)


def bfs(node):
    visited2[node] = True
    q = deque([node])
    while q:
        node = q.popleft()
        print(node, end=" ")
        for i in range(1, n+1):
            if not visited2[i] and graph[node][i]:
                q.append(i)
                visited2[i] = True

    
n, m, v = map(int, sys.stdin.readline().strip().split())
graph = [[False] * (n+1) for _ in range(n+1)] 
visited1 = [False] * (n + 1)
visited2 = [False] * (n + 1)


for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a][b] = True
    graph[b][a] = True
    
dfs(v)
print()
bfs(v)

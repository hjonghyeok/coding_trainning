import sys
from collections import deque

n = int(sys.stdin.readline())
tree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
q = deque()
q.append(1)
tree[1] = 1

while q:
    node = q.popleft()
    for i in graph[node]:
        if not tree[i]:
            q.append(i)
            tree[i] = node

for i in tree[2:]:
    print(i)
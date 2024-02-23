import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())

answer = -1

q = deque()
q.append((a, 1))

while q:
    node, cnt = q.popleft()
    if node == b:
        answer = cnt
        break
    for i in [node*2, node*10+1]:
        if i <= b:
            q.append((i, cnt+1))
    
print(answer)

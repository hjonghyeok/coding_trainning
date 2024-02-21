from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())

L = [0] * (max(n, k)*2 + 1) 


q = deque([n])

while q:
    x = q.popleft()
    if x == k:
        print(L[x])
        break
    for nx in (x-1, x+1, x*2):
        if 0 <= nx < max(n, k)*2 + 1 and not L[nx]:
            L[nx] = L[x] + 1
            q.append(nx)
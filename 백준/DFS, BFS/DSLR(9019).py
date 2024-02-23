import sys
from collections import deque

T = int(input())

for _ in range(T):
    A, B = map(int,sys.stdin.readline().rstrip().split())

    visited = [0 for _ in range(10001)]
    q = deque()
    q.append((A, ''))
    
    while q:
        num, cmd = q.popleft()
        
        if num == B:
            print(cmd)
            break
        
        d = num * 2 % 10000
        if not visited[d]:
            q.append((d, cmd+'D'))
            visited[d] = 1
        
        s = (num - 1) % 10000
        if not visited[s]:
            q.append((s, cmd+'S'))
            visited[s] = 1
        
        l = (num % 1000) * 10 + (num // 1000)
        if not visited[l]:
            q.append((l, cmd+'L'))
            visited[l] = 1
            
        r = (num%10) * 1000 + (num//10)
        if not visited[r]:
            q.append((r, cmd+'R'))
            visited[r] = 1
        
        
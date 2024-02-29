from collections import deque
import sys
sys.setrecursionlimit(2500)
n, k = map(int, sys.stdin.readline().split())
MAX = 100001  
dist = [0] * MAX  
path = [-1] * MAX 

def bfs():
    q = deque([n])
    while q:
        x = q.popleft()
        if x == k:
            return
        for next_x in [x-1, x+1, x*2]:
            if 0 <= next_x < MAX and not dist[next_x]: 
                dist[next_x] = dist[x] + 1
                path[next_x] = x
                q.append(next_x)

def print_path_iterative(x):
    path_stack = []
    while x != n: 
        path_stack.append(x)
        x = path[x]
    path_stack.append(n)  
    while path_stack:  
        print(path_stack.pop(), end=' ')

       
bfs()
print(dist[k])
print_path_iterative(k)

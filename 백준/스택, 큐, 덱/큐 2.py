import sys
from collections import deque

q = deque()

for _ in range(int(sys.stdin.readline().strip())):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        q.append(cmd[1])
    elif cmd[0] == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif cmd[0] == "size":
        if q:
            print(len(q))
        else:
            print(0)
    elif cmd[0] == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif cmd[0] == "front":
        if q: 
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)
        
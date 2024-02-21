import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    s = list(s[1:len(s)-1].split(','))
    q = deque()
    
    error = 0
    r = 1
    for i in s:
        if i != '':
            q.append(i)
    for i in p:
        if i == "R":
            r *= -1
        else:
            if q:
                if r == -1:
                    q.pop()
                else:
                    q.popleft()
            else:
                error = 1
                break
    if error:
        print("error")
    else:
        if r == -1:
            q.reverse()
        print("[" + ','.join(q) + ']')


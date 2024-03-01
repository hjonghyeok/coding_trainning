import sys
from collections import deque
n, w, l = map(int, sys.stdin.readline().split())
truck = deque(list(map(int, sys.stdin.readline().split())))

answer = 0
q = deque([0 for _ in range(w)])

while q:
    answer += 1
    q.popleft()
    if truck:
        if truck[0] + sum(q) <= l:
            q.append(truck.popleft())
        else:
            q.append(0)
print(answer)
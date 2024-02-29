import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
q = deque([i for i in range(1, n + 1)])
targets = list(map(int, sys.stdin.readline().split()))

cnt = 0
for target in targets:
    while True:
        if q[0] == target:
            q.popleft()
            break
        else:
            idx = q.index(target)
            if idx <= len(q) // 2:
                q.rotate(-1)
                cnt += 1
            else:
                q.rotate(1)
                cnt += 1

print(cnt)
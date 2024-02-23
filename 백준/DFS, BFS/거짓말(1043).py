import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = set(sys.stdin.readline().split()[1:])


party = []
for _ in range(m):
    party.append(set(sys.stdin.readline().split()[1:]))

for _ in range(m):
    for i in party:
        if i & arr:
            arr = i | arr

cnt = 0
for i in party:
    if i & arr:
        continue
    cnt += 1
print(cnt)
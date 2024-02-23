import sys
from collections import deque


n, m = map(int, sys.stdin.readline().split())
game = [0] * 101
dic = {}
for _ in range(n+m):
    a, b = map(int, sys.stdin.readline().split())
    dic[a] = b

q = deque()
q.append(1)
game[1] = 1


while q:
    node = q.popleft()
    if node == 100:
        break
    for i in range(1, 7):
        target = node+i
        if (target > 100):
            continue
        if target in dic:
            target = dic.get(target)
        if not game[target]:
            game[target] = game[node] + 1
            q.append(target)

print(game[100]-1)

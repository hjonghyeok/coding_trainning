import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

chicken = []
house = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            house.append((i, j))
        elif maps[i][j] == 2:
            chicken.append((i, j))

answer = float('inf')

def fn1(target):
    count = 0
    for x, y in house:
        count += (min([ abs(x-cx) + abs(y-cy) for cx, cy in target]))
    return count

k = (combinations(chicken, m))
for i in combinations(chicken, m):
    answer = min(answer, fn1(i))
    
print(answer)
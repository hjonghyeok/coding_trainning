import sys

n = int(sys.stdin.readline().strip())
peoples = []
for _ in range(n):
    peoples.append(list(map(int, sys.stdin.readline().strip().split())))
    
rank = [1] * n

for i in range(n):
    for j in range(n):
        if peoples[i][0] < peoples[j][0] and peoples[i][1] < peoples[j][1]:
            rank[i] += 1
for i in rank:
    print(i, end=" ")

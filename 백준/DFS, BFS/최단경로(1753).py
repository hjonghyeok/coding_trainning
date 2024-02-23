import sys, heapq

v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
# tree = [list(map(int, sys.stdin.readline().split()))for _ in range(e)]
tree = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    tree[a].append((b, c))


answers = [float('inf')] * (v+1)
q = []
heapq.heappush(q, (0, k))
answers[k] = 0
while q:
    cost, node = heapq.heappop(q)
    for i in tree[node]:
        if answers[i[0]] > cost+i[1]:
            heapq.heappush(q, (cost+i[1], i[0]))
            answers[i[0]] = cost+i[1]
            
for i in answers[1:]:
    if i == float('inf'):
        print("INF")
    else:
        print(i)
        
import sys

n = int(sys.stdin.readline())

L = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

L.sort(key=lambda x:(x[1], x[0]))

l_end = 0
cnt = 0
for s, e in L:
    if s >= l_end:
        l_end = e
        cnt += 1
print(cnt)
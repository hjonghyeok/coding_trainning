import sys

n = int(sys.stdin.readline().strip())
m = map(int, sys.stdin.readline().split())
m = list(m)
q = [ _ for _ in range(1, n+1)]
arr = []
idx = 0
while len(q) != 0:
    if idx >= len(q):
        idx %= len(q)
    old_idx = idx
    arr.append(q.pop(idx))
    if m[idx] >= 1:
        idx += m[idx] - 1
    else:
        idx -= m[idx] - 1
    m.pop(old_idx)
    print(arr)
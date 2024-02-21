import sys

n = int(sys.stdin.readline().strip())

L = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

b, w = 0, 0

def fn(paper, n):
    global b, w
    s = 0
    for i in paper:
        s += sum(i)
    if s == n**2:
        b += 1
        return
    elif s == 0:
        w += 1
        return
    else:
        fn([paper[i][:n//2] for i in range(n//2)], n//2)
        fn([paper[i][:n//2] for i in range(n//2, n)], n//2)
        fn([paper[i][n//2:] for i in range(n//2)], n//2)
        fn([paper[i][n//2:] for i in range(n//2, n)], n//2)
        
fn(L, n)
print(w)
print(b)
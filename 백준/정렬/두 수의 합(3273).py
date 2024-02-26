import sys

n = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))
x = int(sys.stdin.readline())

cnt = 0

s, e = 0, n-1
while s<e:
    a, b = arr[s], arr[e]
    if a+b == x:
        cnt += 1
        s += 1
        # e -= 1
    elif a+b < x:
        s += 1
    else:
        e -=1
        
print(cnt)

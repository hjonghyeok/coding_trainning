import sys

n, k = map(int, sys.stdin.readline().split())
revels = [int(sys.stdin.readline()) for _ in range(n)]

s = min(revels)
e = s + k
while s <= e:
    mid = (s+e)//2
    cnt = sum(max(0, mid - i) for i in revels)
    if cnt > k:
        e = mid - 1
    else:
        s = mid + 1
        
print(e)
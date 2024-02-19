import sys

k, n = map(int,sys.stdin.readline().strip().split())
rans = [ int(sys.stdin.readline().strip()) for _ in range(k)]

start = 1
end = max(rans)

while start <= end:
    lan = 0
    mid = (start + end) // 2
    
    for i in rans:
        lan += i // mid
    
    if lan >= n:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)

import sys

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
arr = [0] * m

s, e = max(nums), sum(nums)
answer = e

while s<=e:
    mid = (s+e)//2
    
    total = 0
    cnt = 1
    for i in nums:
        if total + i > mid:
            cnt += 1
            total = 0
        total += i
    
    if cnt <= m:
        answer = min(answer, mid)
        e = mid -1
        
    else:
        s = mid + 1
print(answer)
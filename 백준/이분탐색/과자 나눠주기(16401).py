import sys
m, n = map(int, sys.stdin.readline().split())
nums = sorted(map(int, sys.stdin.readline().split()))

s = 1
e = nums[-1]
answer = 0

while s <= e:
    mid = (s + e) // 2
    cnt = 0
    for i in range(n):
        cnt += nums[i]//mid
    if cnt >= m:
        answer = max(mid, answer)
    
    if cnt < m:
        e = mid-1
    else:
        s = mid+1
print(answer)
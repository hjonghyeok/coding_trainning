import sys
n, m = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(m)]

s, e = 1, max(nums)

while s <= e:
    mid = (s+e) // 2
    cnt = 0
    for i in nums:
        if i % mid == 0:
            cnt += i//mid
        else:
            cnt += (i//mid)+1
    
    if cnt > n:
        s = mid + 1
    else:
        e = mid -1
print(s)

import sys

n = int(sys.stdin.readline())
nums = sorted(list(map(int, sys.stdin.readline().split())))

s = 1
e = nums[-1]
answer = 0
while s<e:
    mid = (s+e)//2
    
    for i in range(1, n+1):
        if mid * i > nums[i-1]:
            e = mid - 1
            break
    else:
        answer = mid
        s = mid + 1
    
print(answer)
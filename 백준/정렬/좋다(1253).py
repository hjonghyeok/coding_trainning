import sys

n = int(sys.stdin.readline())
nums = sorted(list(map(int, sys.stdin.readline().split())))

good = 0
for i in range(n):
    target = nums[i]
    s, e = 0, n - 1
    
    while s < e:
        if s == i:
            s += 1
            continue
        if e == i:  
            e -= 1
            continue
        
        current_sum = nums[s] + nums[e]
        
        if current_sum == target:
            good += 1
            break 
        elif current_sum < target:
            s += 1
        else:
            e -= 1

print(good)
import sys

n = int(sys.stdin.readline())
nums = sorted(list(map(int, sys.stdin.readline().split())))

s, e = 0, n-1
answer = nums[s] + nums[e]
min_answer = abs(answer)

while s < e:
    a = nums[s] + nums[e]
    b = abs(a)
    
    if b < min_answer:
        min_answer = b
        answer = a
    
    if a>0:
        e -= 1
    else:
        s += 1
print(answer)
    

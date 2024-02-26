import sys

n = int(sys.stdin.readline())
nums = sorted(list(map(int, sys.stdin.readline().split())))

s = 0
e = len(nums) - 1
ans = float('inf')
answer = [s, e]

while s<e:
    t = (nums[s] + nums[e])
    if  abs(t) < abs(ans):
        ans = nums[s] + nums[e]
        answer[0], answer[1] = s, e
    if t < 0:
        s += 1
    else:
        e -= 1
    
print(nums[answer[0]], nums[answer[1]])
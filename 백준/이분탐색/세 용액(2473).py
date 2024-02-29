import sys

n = int(sys.stdin.readline())
nums = sorted(map(int, sys.stdin.readline().split()))

abs_ans = float('inf')
answers = []

for i in range(n-2):
    mid = nums[i]
    start = i+1
    end = n-1
    while start < end:
        a = mid + nums[start] + nums[end]
        b = abs(a)
        if abs_ans > b:
            abs_ans = b
            answers = [mid, nums[start], nums[end]]
        
        if a > 0:
            end -= 1
        else:
            start += 1

print(*answers)
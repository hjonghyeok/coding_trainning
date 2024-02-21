import sys
nums = [int(sys.stdin.readline().strip()) for _ in range(5)]
nums.sort()
print(int(sum(nums) / len(nums) + 0.5))
print(nums[2])
import sys


n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

stack = []
def DFS():
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return
    
    for i in range(n):
        if nums[i] not in stack:
            stack.append(nums[i])    
            DFS()
            stack.pop()
    
DFS()
import sys


n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

stack = []
def DFS(v):
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return
    
    for i in range(v, n):
        stack.append(nums[i])    
        DFS(i)
        stack.pop()
    
DFS(0)
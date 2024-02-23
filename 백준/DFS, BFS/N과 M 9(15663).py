import sys


n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

stack = []
answer = []

def DFS(v):
    if len(stack) == m:
        ans = " ".join(map(str, stack))
        if ans not in answer:
            answer.append(ans)
            print(ans)
        return
    
    for i in range(v, n):
        stack.append(nums[i])    
        DFS(i)
        stack.pop()

DFS(0)

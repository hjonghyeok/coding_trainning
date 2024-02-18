
 
def dfs(numbers, target, current, idx):
    global cnt
    if idx == len(numbers):
        if current == target:
            cnt += 1
        return
 
    dfs(numbers, target, current + numbers[idx], idx + 1)
    dfs(numbers, target, current - numbers[idx], idx + 1)
 
def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return cnt

cnt = 0
print(solution([1,1,1,1,1], 3))
cnt = 0
print(solution([4,1,2,1], 4))

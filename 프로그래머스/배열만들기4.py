def solution(arr):
    stk = []
    i = 0
    
    while i <= len(arr):
        if stk == []:
            stk.append(arr[i])
            i += 1
            continue
        if stk[-1] < arr[i]:
            print(stk[-1])
            stk.append(arr[i])
            i += 1
        else:
            stk.pop()

print(solution([1,4,2,5,3]))
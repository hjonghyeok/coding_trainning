def solution(arr):
    answer = []
    tmp = -1
    for i in arr:
        if tmp != i:
            answer.append(i)
            tmp = i
    return answer

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))
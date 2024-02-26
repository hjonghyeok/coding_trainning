def solution(score):
    answer = []
    arr = []
    for i in range(len(score)):
        arr.append(sum(score[i])/2)
        answer.append(sum(score[i])/2)
    answer.sort(reverse = 1)
    for i in range(len(arr)):
        arr[i] = answer.index(arr[i])+1
    
    return arr

print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]))
print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))
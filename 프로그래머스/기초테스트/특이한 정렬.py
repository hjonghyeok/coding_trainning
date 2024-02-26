def solution(numlist, n):

    arr = []
    for i in numlist:
        arr.append([abs(n-i), i])
    arr.sort(key=lambda x:(x[0], -x[1]))
    answer = []
    for i in arr:
        answer.append(i[1])
    
    return answer

print(solution([1, 2, 3, 4, 5, 6], 4))
print(solution([10000,20,36,47,40,6,10,7000], 30))
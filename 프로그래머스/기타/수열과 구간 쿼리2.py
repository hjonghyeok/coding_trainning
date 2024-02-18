def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        arr2 = arr[s:e+1]
        arr2.sort()
        for i in arr2:
            if i > k:
                answer.append(i)
                break
        else:
            answer.append(-1)

    return answer

print(solution([0, 1, 2, 4, 3], [[0, 4, 2],[0, 3, 2],[0, 2, 2]]))
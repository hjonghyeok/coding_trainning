def solution(num_list, n):
    answer = []
    r = []
    for i in range(len(num_list)):
        r.append(num_list[i])
        if len(r) == n:
            answer.append(r)
            r = []
        
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2))
print(solution([100, 95, 2, 4, 5, 6, 18, 33, 948], 3))
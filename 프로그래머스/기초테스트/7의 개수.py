def solution(array):
    answer = 0
    for i in array:
        if '7' in str(i):
            answer += str(i).count('7')
    return answer

print(solution([7, 77, 17]))
print(solution([10, 29]))

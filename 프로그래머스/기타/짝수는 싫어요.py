def solution(n):
    answer = []
    for i in range(1, n+1, 2):
            answer.append(i)
    return answer

print(solution(10))
print(solution(15))
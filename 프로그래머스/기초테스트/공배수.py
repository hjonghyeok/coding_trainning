def solution(number, n, m):
    answer = 0

    if not (number % n) and not (number % m):
        answer = 1
    return answer

print(solution(60, 2, 3))
print(solution(55, 10, 5))
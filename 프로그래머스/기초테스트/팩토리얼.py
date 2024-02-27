def solution(n):
    answer = 1
    f = 1
    while 1:
        f *= answer
        if f > n:
            break
        answer += 1
    return answer -1

print(solution(3628800))
print(solution(7))
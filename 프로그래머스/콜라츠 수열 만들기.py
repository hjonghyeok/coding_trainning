def solution(n):
    answer = [n]
    while 1:
        if n % 2:
            n = 3*n+1
        else:
            n = n//2
        answer.append(int(n))
        if n == 1:
            break
    return answer

print(solution(10))
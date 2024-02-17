def solution(n):
    answer = 0
    if n%2:
        answer = sum(range(1, n+1, 2))
        return answer
    else:
        for i in range(2, n, 2):
            answer += i**2
        return answer+n**2
        

print(solution(7))
print(solution(10))
def solution(balls, share):
    n = 1
    x = 1
    m = 1
    for i in range(1, balls+1):
        n *= i
    for i in range(1, balls-share+1):
        x *= i
    for i in range(1, share+1):
        m *= i
    answer = n//(x*m)
    return answer

print(solution(3, 2))
print(solution(5, 3))
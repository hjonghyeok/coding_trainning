def solution(n):
    for i in range(1, n * 6 + 1, 1):
        if (6*i)%n==0:
            return i
    


print(solution(6))
print(solution(10))
print(solution(4))
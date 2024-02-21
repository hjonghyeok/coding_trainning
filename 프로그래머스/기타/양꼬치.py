def solution(n, k):
    answer = 12000 * n + (k - (n//10)) * 2000
    return answer

print(solution(10, 3))
print(solution(64, 6))
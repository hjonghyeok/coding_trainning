def solution(a, b):
    answer = max(int(f"{a}{b}"), 2*a*b)
    return answer

print(solution(2, 91))
print(solution(91, 2))

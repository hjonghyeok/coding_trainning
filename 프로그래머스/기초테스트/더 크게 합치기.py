def solution(a, b):
    answer = max(f"{a}{b}", f"{b}{a}")
    return int(answer)

print(solution(9, 91))
print(solution(89, 8))
print(solution(9999, 9993))
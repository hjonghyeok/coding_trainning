def solution(brown, yellow):
    total = brown + yellow
    for i in range(3, int(total**0.5)+1):
        if not (total % i):
            w = total // i
            if (w-2) * (i-2) == yellow:
                return w, i


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
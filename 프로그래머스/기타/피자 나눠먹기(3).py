def solution(slice, n):
    for i in range(1, slice*n):
        if (i * slice) // n >= 1:
            return i

print(solution(7, 10))
print(solution(4, 12))
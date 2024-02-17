def solution(numbers):
    A = list(map(str, numbers))
    A.sort(key = lambda x:x*3, reverse=1)
    return str(int(''.join(A)))

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
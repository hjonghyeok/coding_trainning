def solution(numbers, k):
    answer = 1
    cnt = 0
    while answer < k:
        cnt += 2
        answer += 1
        if cnt >= len(numbers):
            cnt = cnt % len(numbers)
    return numbers[cnt]

print(solution([1,2,3,4], 2))
print(solution([1,2,3,4,5,6], 5))
print(solution([1,2,3], 3))
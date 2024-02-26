from itertools import permutations

# 소수 판별 함수
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    perms = set()  # 중복을 제거하기 위해 집합 사용

    # 가능한 모든 숫자 조합 생성
    for l in range(1, len(numbers)+1):
        for p in permutations(numbers, l):
            num = int(''.join(p))
            perms.add(num)

    # 소수 판별
    for num in perms:
        if is_prime(num):
            answer += 1

    return answer

print(solution("17"))
print(solution("001"))
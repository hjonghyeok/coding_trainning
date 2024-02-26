def solution(a, b):
    if a % b == 0:
        return 1
    c = 1
    for i in range(min(a, b), 0, -1):
        if a%i == 0 and b%i==0:
            c = i
            break
    b = b//c
    for i in [2, 5]:
        while b % i == 0:
            b = b//i
    if b != 1:
        return 2
    return 1

print(solution(3, 11))
print(solution(11, 22))
print(solution(12, 21))
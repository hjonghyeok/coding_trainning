def solution(a, b, flag):
    if flag:
        return a + b
    return a-b

print(solution(-4, 7, True))
print(solution(-4, 7, False))
def solution(sides):
    b = max(sides) - max(sides) - min(sides)
    c = sum(sides)-1 - max(sides)
    return b+c

print(solution([1,2]))
print(solution([3,6]))
print(solution([11,7]))
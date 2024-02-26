def solution(dots):
    a, b = [], []
    for i, j in dots:
        a.append(i)
        b.append(j)
    
    answer = (max(a) - min(a)) * (max(b) - min(b))
    return answer

print(solution([[1, 1], [2, 1], [2, 2], [1, 2]]))
print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]))
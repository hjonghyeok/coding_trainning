def solution(num_list):
    c1, c2 = 0, 0
    for i in num_list:
        if i%2:
            c2 += 1
        else:
            c1 += 1
    return [c1, c2]

print(solution([1,2,3,4,5]))
print(solution([1,3,5,7]))
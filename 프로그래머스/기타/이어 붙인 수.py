def solution(num_list):
    a1 = ''
    a2 = ''
    for i in num_list:
        if i%2:
            a1 += str(i)
        else:
            a2 += str(i)
    return int(a2) + int(a1)
    

print(solution([3, 4, 5, 2, 1]))
print(solution([5, 7, 8, 3]))
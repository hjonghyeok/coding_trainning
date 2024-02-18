def solution(array):
    array2 = set(array)
    number = []
    for i in array2:
        number.append(array.count(i))
    array2 = list(array2)
    if number.count(max(number)) > 1:
        return -1
    else:
        return array2[number.index(max(number))]
        
        

print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 2, 2]))
print(solution([1, 1, 1, 1]))
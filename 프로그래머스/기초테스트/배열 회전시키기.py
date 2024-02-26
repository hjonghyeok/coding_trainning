def solution(numbers, direction):
    answer = []
    if direction == "right":
        answer = numbers[:-1]
        answer.insert(numbers[-1], 0)
    else:
        answer = numbers[1:]
        answer.append(numbers[0])
        
    return answer

print(solution([1, 2, 3], "right"))
print(solution([4, 455, 6, 4, -1, 45, 6], "left"))
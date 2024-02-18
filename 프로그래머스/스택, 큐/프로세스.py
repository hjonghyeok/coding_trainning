
def solution(priorities, location):
    
    place = priorities.index(max(priorities))
    answer = 0
    while 1:
        if priorities[place] == max(priorities):
            priorities[place] = -1
            answer += 1
        
            if place == location:
                break
        place += 1
        if place >= len(priorities):
            place = 0

    return answer

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))


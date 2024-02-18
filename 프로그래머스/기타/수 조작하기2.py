def solution(numLog):
    answer = ''
    num = numLog[0]
    for i in range(1, len(numLog)):
        if num - numLog[i] == -1: answer += 'w'
        elif num - numLog[i] == 1: answer += 's'
        elif num - numLog[i] == 10: answer += 'a'
        elif num - numLog[i] == -10: answer += 'd'
        num = numLog[i]
        
    return answer

print(solution([0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]))
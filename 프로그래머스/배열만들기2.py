def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if set(str(i)) - set(['0', '5']):
            continue
        answer.append(i)
    if answer == []:
        answer.append(-1)
    return answer 

print(solution(5,555))
print(solution(10,20))
def solution(a, d, included):
    answer = 0
    for i, t in enumerate(included):
        if t:
            answer += a + d*i
    
    return answer

print(solution(3,4,[True, False, False, True, True]))
print(solution(7,1,[False,False,False,True,False,False,False]))

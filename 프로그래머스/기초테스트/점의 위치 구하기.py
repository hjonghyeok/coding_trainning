def solution(dot):
    answer = 0
    x, y = dot[0], dot[1]
    if x>0 and y>0:
        answer = 0
    elif x<0 and y>0:
        answer = 2
    elif x<0 and y<0:
        answer = 3
    else:
        answer = 4
    return answer

print(solution([2, 4]))
print(solution([-7, 9]))
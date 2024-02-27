def solution(my_string):
    arr = my_string.split(' ')
    answer = 0
    a = True
    for i in range(len(arr)):
        if i%2:
            if arr[i] == '+':
                a = True
            else:
                a = False
        else:
            if a:
                answer+=int(arr[i])
            else:
                answer-=int(arr[i])
    return answer

print(solution("3 + 4"))
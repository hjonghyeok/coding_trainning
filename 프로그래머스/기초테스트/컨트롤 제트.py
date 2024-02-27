def solution(s):
    answer = 0
    arr = s.split(' ')
    last = int(arr[0])
    for i in arr:
        if i == 'Z':
            answer -= last
        else:
            answer += int(i)
            last = int(i)
        
    return answer

print(solution("1 2 Z 3"))
print(solution("10 20 30 40"))
print(solution("10 Z 20 Z 1"))
print(solution("10 Z 20 Z"))
print(solution("-1 -2 -3 Z"))
def solution(num, total):
    answer = []
    if num % 2:
        c = total // num
        answer.append(c)
        for i in range(1, (num-1)//2+1):
            answer.append(c+i)
            answer.append(c-i)
    else:
        c = total // num
        answer.append(c)
        for i in range(1, (num-1)//2+2):
            answer.append(c+i)
        for i in range(1, (num-1)//2+1):
            answer.append(c-i)
            
    answer.sort()
    return answer

print(solution(3, 12))
print(solution(5, 15))
print(solution(4, 14))
print(solution(5, 5))
print(solution(10, 55))
def solution(price):
    answer = price
    if answer >= 500000:
        answer *= 0.8
    elif answer >= 300000:
        answer *= 0.9
    elif answer >= 100000:
        answer *= 0.95
        
    return int(answer)

print(solution(150000))
print(solution(580000))
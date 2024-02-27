def solution(numbers):
    dic = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    answer = []
    while numbers:
        for i, j in dic.items():
            if not numbers:
                break
            if i == numbers[:len(i)]:
                answer.append(j)
                numbers = numbers[len(i):]
    return int(''.join(map(str, answer)))

print(solution("onetwothreefourfivesixseveneightnine"))
print(solution("onezerofourzerosixseven"))
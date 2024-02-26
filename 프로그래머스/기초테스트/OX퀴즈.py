def solution(quiz):
    answer = []
    arr = []
    for i in quiz:
        arr.append(i.split())
    for i in arr:
        result = int(i[0])
        s = ''
        for j in i[1:]:
            if j == '=':
                break
            if j in '+-':
                s = j
            else:
                if s == '+':
                    result += int(j)
                else:
                    result -= int(j)
        if result == int(i[-1]):
            answer.append("O")
        else:
            answer.append("X")
            
    return answer

print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))

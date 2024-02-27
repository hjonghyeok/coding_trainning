def solution(s):
    answer = ''
    a = ''
    for i in s:
        if i not in answer and i not in a:
            answer += i
        elif i in answer or i in a:
            answer = answer.replace(i, '')
            a += i
    answer = sorted(list(answer))
    return ''.join(answer)

print(solution("abcabcadc"))
print(solution("abdc"))
print(solution("hello"))
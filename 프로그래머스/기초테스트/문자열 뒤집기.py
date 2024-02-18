def solution(my_string):
    answer = list(my_string)
    return ''.join(answer[::-1])

print(solution("jaron"))
print(solution("bread"))
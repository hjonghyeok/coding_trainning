def solution(my_string):
    s = 'aeiou'
    for i in s:
        my_string = my_string.replace(i, '')
    return my_string

print(solution("bus"))
print(solution("nice to meet you"))
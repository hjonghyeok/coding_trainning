def solution(my_string, overwrite_string, s):
    LIST_MY_STRING = list(my_string)
    for i in range(s, s + len(overwrite_string), 1):
        LIST_MY_STRING[i] = overwrite_string[i-s]
    answer = ''.join(LIST_MY_STRING)
    return answer

print(solution("He11oWor1d", "lloWorl", 2))
print(solution("Program29b8UYP", "merS123", 7))
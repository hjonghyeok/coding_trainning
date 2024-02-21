def solution(my_string, letter):
    return ''.join(my_string.split(letter))

print(solution("abcdef", "f"))
print(solution("BCBdbe", "B"))
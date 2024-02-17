def solution(s):
    answer = 0
    while 1:
        c1 = 0
        c2 = 0
        x = s[0]
        for i in range(len(s)):
            if s[i] == x:
                c1 += 1
            else:
                c2 += 1
            if c1 == c2:
                answer += 1
                s = s[i+1:]
                break
            elif i+1 == len(s):
                answer += 1
                s = ''
                break
        if s == '':
            break

    return answer

print(solution("banana"))
print(solution("abracadabra"))
print(solution("aaabbaccccabba"))
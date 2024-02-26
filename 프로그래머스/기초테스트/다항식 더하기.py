def solution(polynomial):
    arr = polynomial.split()
    a = [0] * 2
    answer = ''
    for i in arr:
        if 'x' in i:
            if len(i) >= 2:
                a[0] += int(i[:-1])
            else:
                a[0] += 1
        elif i == '+':
            pass
        else:
            a[1] += int(i)
    
    if not a[0]:
        return str(a[1])
    elif not a[1]:
        if a[0] == 1:
            return 'x'
        else:
            return str(a[0]) + 'x'
    else:
        if a[0] == 1:
            return 'x' + ' + ' + str(a[1])
        return str(a[0]) + 'x' + ' + ' + str(a[1])


print(solution("3x + 7 + x"))
print(solution("7 + 8 + 9 + x"))
print(solution("x + x + 24 + x + 10x + 2"))
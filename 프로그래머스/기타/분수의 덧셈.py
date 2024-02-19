def solution(numer1, denom1, numer2, denom2):
    c = 0
    for i in range(max(denom1,denom2), (denom1*denom2)+1):
        if i % denom1 == 0 and i % denom2 == 0:
            c = i
            break
    answer = [numer1*c//denom1 + numer2*c//denom2, max(denom1,denom2) * c//max(denom1,denom2)]
    return answer

print(solution(1,2,3,4))
print(solution(9,2,1,3))
def solution(bin1, bin2):
    b1 = int(bin1, 2)
    b2 = int(bin2, 2)
    b = b1+b2

    return (bin(b))[2:]


print(solution("10", "11"))
print(solution("1001", "1111"))
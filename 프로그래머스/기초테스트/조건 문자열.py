def solution(ineq, eq, n, m):
    ineq += eq
    if ineq == ">=":
        answer = n >= m
    elif ineq == "<=":
        answer = n <= m
    elif ineq == ">!":
        answer = n > m
    else:
        answer = n < m
    return int(answer)

print(solution("<","=","20","50"))
print(solution(">","!","41","78"))
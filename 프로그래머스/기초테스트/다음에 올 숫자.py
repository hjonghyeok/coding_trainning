def solution(common):
    if common[-2] - common[-3] == common[-1] - common[-2]:
        return common[-1] - common[-2] + common[-1]
    else:
        return common[-1] * (common[-1] // common[-2])



print(solution([1,2,3,4]))
print(solution([2,4,8]))
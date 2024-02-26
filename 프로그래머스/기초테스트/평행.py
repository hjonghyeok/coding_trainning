def solution(dots):
    for i in range(3):
        if i == 0:
            p1, p2, p3, p4 = dots[0], dots[1], dots[2], dots[3]
        elif i == 1:
            p1, p2, p3, p4 = dots[0], dots[2], dots[1], dots[3]
        else:
            p1, p2, p3, p4 = dots[0], dots[3], dots[1], dots[2]

        if (p2[1] - p1[1]) * (p4[0] - p3[0]) == (p4[1] - p3[1]) * (p2[0] - p1[0]):
            return 1
        
    return 0


print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))
print(solution([[3, 5], [4, 1], [2, 4], [5, 10]]))
print(solution([[3, 5], [3, 5], [2, 4], [2, 4]]))
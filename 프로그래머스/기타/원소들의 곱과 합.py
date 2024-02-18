from math import prod
def solution(num_list):
    return int(sum(num_list) ** 2 > prod(num_list))

print(solution([3, 4, 5, 2, 1]))
print(solution([5, 7, 8, 3]))
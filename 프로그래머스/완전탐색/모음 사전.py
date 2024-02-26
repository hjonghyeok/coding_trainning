from itertools import permutations, product

def solution(word):
    a = ["A", "E", "I", "O", "U"]
    arr = []
    for i in range(1, 6):
        for j in product(a, repeat=i):
            arr.append(''.join(j))
    arr.sort()

    return arr.index(word) + 1

print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))
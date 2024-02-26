def solution(board):
    coordinate = set()
    n = len(board)
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == 1:
                for x in (-1, 0, 1):
                    for y in (-1, 0, 1):
                        if -1 < i + x < n and -1 < j + y < n:
                            coordinate.add((i + x, j + y))
    return n * n - len(coordinate)

print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))
print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))
def solution(arr, queries):
    for i, j in queries:
        arr[i], arr[j] = arr[j], arr[i]

    return arr

print(solution([0, 1, 2, 3, 4], [[0, 3],[1, 2],[1, 4]]))
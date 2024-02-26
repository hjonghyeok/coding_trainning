def solution(sizes):
    w, h = max(map(max, sizes)), 0

    for i in sizes:
        if h < min(i):
            h = min(i)
    return w * h

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
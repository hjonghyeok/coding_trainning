def solution(distance, rocks, n):
    rocks.sort()
    s, e = 0, distance
    answer = 0
    
    while s<=e:
        mid = (s+e) // 2
        cnt, start, old_start = 0,0,0
        for rock in rocks:
            if rock - start < mid:
                cnt += 1
            else:
                start, old_start = rock, start
        
        if rocks[-1] == start:
            if distance - start < mid:
                cnt += 1
                start = old_start
        if n < cnt:
            e = mid - 1
        else:
            s = mid + 1
            answer = mid
    return answer

print(solution(25,[2, 14, 11, 21, 17], 2))
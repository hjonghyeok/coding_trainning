def solution(n, times):
    answer = 0
    start = 0
    end = max(times) * n

    
    while start <= end:
        mid = (start+end) // 2
        people = 0
        for i in times:
            people += mid // i
            if people >= n:
                break
        if people >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer

print(solution(6, [7,10]))
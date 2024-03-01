def solution(n):
    answer = 0
    for i in range(1, n):
        cnt = 0
        for j in range(i, n//2+2):
            cnt += j
            if cnt >= n:
                if cnt == n:
                    answer += 1
                break
    return answer+1

while 1:
    print(solution(int(input())))
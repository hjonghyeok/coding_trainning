from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for i in permutations(dungeons, len(dungeons)):
        p = k
        cnt = 0
        for j in i:
            if p < j[0]:
                break
            else:
                p -= j[1]
                cnt += 1
        answer = max(cnt, answer)
    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))
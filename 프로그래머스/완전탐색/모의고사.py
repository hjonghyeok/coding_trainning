def solution(answers):
    answer = []
    Human = {}
    h1 = [1,2,3,4,5]
    h2 = [2,1,2,3,2,4,2,5]
    h3 = [3,3,1,1,2,2,4,4,5,5]
    hc = 0
    for i in [h1, h2, h3]:
        hc += 1
        count = 0
        for j in range(len(answers)):
            if i[j] == answers[j%len(i)]:
                count+=1
        Human[hc] = count
    Human = dict(sorted(Human.items(), key=lambda x:x[1], reverse=1))
    count = 0
    for k, v in Human.items():
        if count > v:
            break
        count = v
        answer.append(k)
    answer.sort()
        
    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
print(solution([1,1,1,1,1]))
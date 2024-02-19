
def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    str_list = [[] for _ in range(len(id_list))]
    for R in report:
        S = R.split()
        if S[0] not in str_list[id_list.index(S[1])]:
            str_list[id_list.index(S[1])].append(S[0])
        
    for i in str_list:
        if len(i) >= k:
            for j in i:
                answer[id_list.index(j)] += 1
    return answer

print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
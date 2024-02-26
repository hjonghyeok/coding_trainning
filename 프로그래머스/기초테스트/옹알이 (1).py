def solution(babbling):
    answer = 0
    arr = ["aya", 'ye', "woo", "ma"]
    for i in babbling:
        w = ''
        cnt = 0
        for j in i:
            w += j
            if w in arr:
                w = ''
                cnt += 1
        if len(w) == 0 and cnt > 0:
            answer += 1
    return answer

print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))
def solution(spell, dic):
    answer = 2
    
    
    for i in dic:
        for j in spell:
            if j not in i:
                break
        else:
            answer = 1
    return answer

print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))
print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))
print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]))
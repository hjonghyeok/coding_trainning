def solution(id_pw, db):
    answer = 'fail'
    for i, p in db:
        if i == id_pw[0]:
            if p == id_pw[1]:
                return 'login'
            else:
                answer = 'wrong pw'
    return answer

print(solution(["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))
print(solution(["programmer01", "15789"], [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]))
print(solution(["rabbit04", "98761"], [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]))
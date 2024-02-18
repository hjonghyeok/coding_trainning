# def solution(X, Y):
#     X_LIST = list(X)
#     Y_LIST = list(Y)
#     answer = ''
#     X_LIST.sort(reverse=1)
#     Y_LIST.sort(reverse=1)
#     if len(X_LIST) > len(Y_LIST):
#         for i in Y_LIST:
#             if i in X_LIST:
#                 answer += i
#                 X_LIST.remove(i)
#     else:
#         for i in X_LIST:
#             if i in Y_LIST:
#                 answer += i
#                 Y_LIST.remove(i)
#     if answer == '':
#         answer = -1
#     else:
#         answer = int(answer)
#     return str(answer)

def solution(X, Y):
    answer = []
    for i in (set(X)&set(Y)) :
        for j in range(min(X.count(i), Y.count(i))) :
            answer.append(i)
    answer.sort(reverse=True)
    if len(answer) == 0:
        return "-1"
    if answer[0] == "0":
        return "0"
    answer = "".join(answer)
    return answer

print(solution("100", "2345"))
print(solution("100", "203045"))
print(solution("100", "123450"))
print(solution("12321", "42531"))
print(solution("5525", "1255"))
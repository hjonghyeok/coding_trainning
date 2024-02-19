# def solution(participant, completion):
#     ANS = participant.copy()
#     for i in completion:
#         if i in participant:
#             ANS.remove(i)
#     answer = ANS[0]
#     return answer


# def solution(participant, completion):
#     participant.sort()
#     completion.sort()

#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
        
#     return participant[len(participant)-1]

import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer)[0]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]	))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
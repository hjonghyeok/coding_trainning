from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    answer = 0
    visited = [0] * len(words)
    q = deque()
    q.append((begin, 0))
    while q:
        w, cost = q.popleft()
        if w == target:
            return cost
        for i in range(len(words)):
            cnt = 0
            if not visited[i]:
                for j in range(len(words[i])):
                    if w[j] != words[i][j]:
                        cnt += 1
            if cnt == 1:
                q.append((words[i], cost + 1))
                visited[i] = 1

    return 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
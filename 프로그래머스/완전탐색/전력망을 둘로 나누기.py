def dfs(node):
    global visited, tree
    if visited[node]:
        return
    visited[node] = 1
    for i in tree:
        if i[0] == node:
            visited[i[1]] == 1
            dfs(i[1])
        elif i[1] == node:
            visited[i[0]] == 1
            dfs(i[0])
             

def solution(n, wires):
    global visited, tree
    cnt = float('inf')
    for i in range(len(wires)):
        v1 = wires[i][0]
        visited = [0] * (n+1)
        tree = wires[:i] + wires[i+1:]
        dfs(v1)
        s1 = sum(visited)
        s2 = n - s1
        if cnt > abs(s2 - s1):
            cnt = abs(s2 - s1)
    return cnt

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))
def dfs(i, j, visited, maps, n, m):
    global cnt
    if i == n and j == m:
        visited[i][j] = 1
        return cnt
    # if not visited[i][j] and maps[i][j]:
    if maps[i][j] and visited[i][j] < cnt :
        cnt += 1
        visited[i][j] = cnt
        print(cnt)
        dfs(i+1, j, visited, maps, n, m)
        dfs(i-1, j, visited, maps, n, m)
        dfs(i, j+1, visited, maps, n, m)
        dfs(i, j-1, visited, maps, n, m)

def solution(maps):
    n, m = len(maps), len(maps[0])
    for i in maps:
        i.append(0)
        i.insert(0, 0)
    maps.insert(0, [0] * (len(maps[0])))
    maps.append([0] * (len(maps[0])))
    
    visited = [[0] * len(maps[0]) for i in range(len(maps))]
    
    Answers = []
    Answers.append(dfs(1, 1, visited, maps, n, m))
    answer = 0
    
    return Answers

cnt = 1
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
cnt = 0
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
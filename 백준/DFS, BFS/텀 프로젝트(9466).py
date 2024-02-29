import sys
sys.setrecursionlimit(10**6)

def dfs(start):
    global result
    visited[start] = True
    cycle.append(start) # 현재 방문한 노드를 사이클에 추가
    next = nums[start]

    if visited[next]: # 다음 노드를 이미 방문했다면
        if next in cycle: # 사이클이 형성되었는지 확인
            result += cycle[cycle.index(next):] # 사이클에 포함된 노드들만 결과에 추가
        return
    else:
        dfs(next)

for _ in range(int(input())):
    n = int(input())
    nums = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    result = []

    for i in range(1, n+1):
        if not visited[i]: # 방문하지 않은 노드에 대해 DFS 실행
            cycle = []
            dfs(i)

print(n - len(result))   

# DFS 메서드 정의
def dfs (graph, node, visited):
    # 해당 노드를 방문 처리
    visited[node] = True
    # 탐색 순서 출력
    print(node, end = ' ')
    # 한 노드로부터 인접한 다른 노드를 재귀적으로 방문 처리
    for i in graph[node]:
        if not visited[i]:
            dfs(graph, i, visited)
            
graph = [
    [],
    [2, 3],
    [1, 8],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7, 8],
    [6, 8],
    [2, 6, 7]
]
print(graph)
# 노드별로 방문 정보를 리스트로 표현
visited = [False] * 9

# 정의한 DFS 메서드 호출(노드 1을 탐색 시작 노드로 설정)
dfs(graph, 1, visited)
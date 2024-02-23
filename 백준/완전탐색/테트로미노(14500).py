n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
result = 0

# 테트로미노를 제외한 나머지 모양에 대한 DFS 탐색
def dfs(x, y, depth, total):
    global result
    if depth == 4:
        result = max(result, total)
        return
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, depth + 1, total + board[nx][ny])
            visited[nx][ny] = 0

# 'ㅗ' 모양을 위한 별도의 처리 함수
def check_exception(x, y):
    global result
    # 'ㅗ' 모양의 중심을 기준으로 하는 4가지 경우
    exception_cases = [
        [(0, 0), (0, -1), (0, 1), (-1, 0)],
        [(0, 0), (0, -1), (0, 1), (1, 0)],
        [(0, 0), (1, 0), (-1, 0), (0, -1)],
        [(0, 0), (1, 0), (-1, 0), (0, 1)]
    ]
    for case in exception_cases:
        temp = 0
        for dx, dy in case:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                temp += board[nx][ny]
            else:
                break
        result = max(result, temp)

# 메인 로직
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 1, board[i][j])
        visited[i][j] = 0
        check_exception(i, j)

print(result)
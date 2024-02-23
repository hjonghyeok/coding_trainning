T = int(input())

for _ in range(T):
    M, N, X, Y = map(int, input().split())
    X -= 1  # 0 인덱스 기반 조정
    Y -= 1
    is_found = False
    for i in range(X, M*N+1, M):
        if i % N == Y:
            print(i + 1)  # 1 인덱스로 조정
            is_found = True
            break
    if not is_found:
        print(-1)
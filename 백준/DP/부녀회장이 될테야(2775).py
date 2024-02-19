import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    k = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    dp = [[0] * n for _ in range(k)]
    dp.insert(0, [i for i in range(1, n+1)])
    for i in range(1, k+1):
        for j in range(n):
            if j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
    print(dp[k][n-1])
        
    
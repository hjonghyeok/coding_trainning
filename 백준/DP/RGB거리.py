import sys

n = int(sys.stdin.readline())
dp = [[0] * 3 for _ in range(n)]

cost = []
for _ in range(n):
    cost.append(list(map(int, sys.stdin.readline().split())))

dp[0][0], dp[0][1], dp[0][2] = cost[0][0], cost[0][1], cost[0][2]
# 0:R, 1:G, 2:B
for i in range(1, n):
    dp[i][0] += min(dp[i-1][1] + cost[i][0], dp[i-1][2] + cost[i][0])
    dp[i][1] += min(dp[i-1][0] + cost[i][1], dp[i-1][2] + cost[i][1])
    dp[i][2] += min(dp[i-1][1] + cost[i][2], dp[i-1][0] + cost[i][2])
    
print(min(dp[n-1]))

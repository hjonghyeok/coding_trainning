import sys


n, k = map(int, sys.stdin.readline().split())
dp = [[0] * (k+1) for _ in range(n+1)]

items = []
for _ in range(n):
    weight, value = map(int, sys.stdin.readline().split())
    items.append((weight, value))

for i in range(1, n+1):
    weight, value = items[i-1]
    for w in range(1, k+1):
        if weight <= w:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)
        else:
            dp[i][w] = dp[i-1][w]

print(dp[n][k])
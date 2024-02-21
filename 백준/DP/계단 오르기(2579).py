import sys
n = int(sys.stdin.readline().strip())
L = [ int(sys.stdin.readline().strip()) for _ in range(n)]

dp = [0] * (n+1)

dp[1] = L[0]
if n > 1:
    dp[2] = L[1] + L[0]

for i in range(3, n+1):
    a = dp[i-3] + L[i-2] + L[i-1]
    b = dp[i-2] + L[i-1]
    dp[i] = max(a, b)

print(dp[-1])

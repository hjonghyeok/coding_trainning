import sys

n = int(sys.stdin.readline())
dp = [1, 3]
answer = 3
for i in range(2, n+1):
    answer = (dp[1]*2 + dp[0]) % 9901
    dp[0] = dp[1]
    dp[1] = answer
print(answer)
import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    nums = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]
    
    dp[0][0] = nums[0][0]
    dp[1][0] = nums[1][0]
    if n == 1:
        print(max(dp[1][0], dp[0][0]))
        continue
    
    dp[1][1] = dp[0][0] + nums[1][1]
    dp[0][1] = dp[1][0] + nums[0][1]
    if n == 2:
        print(max(dp[1][1], dp[0][1]))
        continue
    
    for i in range(2, n):
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + nums[1][i]
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + nums[0][i]
    print(max(dp[1][-1], dp[0][-1]))
        
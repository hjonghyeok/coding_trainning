import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [arr[0]]
for i in range(1, n):
    dp.append(max(dp[i-1]+arr[i], arr[i]))

print(max(dp))
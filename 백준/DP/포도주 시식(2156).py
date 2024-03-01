import sys

n = int(sys.stdin.readline())
arr = [0]
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
dp = [0 for _ in range(n+1)]

if n > 0:
    dp[1] = arr[1]
if n > 1:
    dp[2] = arr[1] + arr[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-2]+arr[i], arr[i]+arr[i-1]+dp[i-3])

print(max(dp))
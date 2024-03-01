import sys

n = int(sys.stdin.readline().strip())
dp = [0] * (n+1)
arr = [0] * (n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    arr[i] = i-1

    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
        arr[i] = i//2

    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1
        arr[i] = i//3


print(dp[n])
path = []
answer = n
while answer != 0:
    path.append(answer)
    answer = arr[answer]
print(' '.join(map(str, path)))
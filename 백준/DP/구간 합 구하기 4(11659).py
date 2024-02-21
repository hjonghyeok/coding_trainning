import sys

n, m = map(int, sys.stdin.readline().strip().split())
nums = list(map(int, sys.stdin.readline().strip().split()))

sums = [0] * (n+1)
for i in range(1, n+1):
    sums[i] = sums[i-1] + nums[i-1]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().strip().split())
    print(sums[j] - sums[i-1])
import sys
n, m = map(int, sys.stdin.readline().split())
nums = sorted([int(sys.stdin.readline()) for _ in range(n)])

s, e = 0, 0
answer = float('inf')

while e < n and s < n:
    a = nums[e] - nums[s]
    if a >= m:
        answer = min(answer, a)
        s += 1
    else:
        e += 1
print(answer)
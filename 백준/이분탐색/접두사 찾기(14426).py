import sys
from bisect import bisect_left

n, m = map(int, sys.stdin.readline().rstrip().split())
arr1 = sorted([sys.stdin.readline().rstrip() for _ in range(n)])
arr2 = sorted([sys.stdin.readline().rstrip() for _ in range(m)])

arr1.sort()

answer = 0

for i in arr2:
    idx = bisect_left(arr1, i)
    if idx < n and arr1[idx].startswith(i):
        answer += 1
print(answer)
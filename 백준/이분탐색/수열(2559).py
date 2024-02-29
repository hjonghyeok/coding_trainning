n, k = map(int, input().split())
nums = list(map(int, input().split()))

# 누적 합 배열 계산
prefixSum = [0] * (n+1)
for i in range(1, n+1):
    prefixSum[i] = prefixSum[i-1] + nums[i-1]

# 연속된 k일의 최대 온도 합 찾기
answer = -float('inf')
for i in range(k, n+1):
    tempSum = prefixSum[i] - prefixSum[i-k]
    answer = max(answer, tempSum)

print(answer)
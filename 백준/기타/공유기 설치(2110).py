n, c = map(int, input().split())
pos = [int(input()) for _ in range(n)]
pos.sort()

start = 1
end = pos[-1] - pos[0]
result = 0
if c == 2:
    print(pos[-1] - pos[0])
else:
    while start<=end:
        mid = (start+end) // 2
        count = 1
        
        ts = pos[0]
        for i in pos:
            if i - ts >= mid:
                count += 1
                ts = i
        if count >= c:
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    print(result)
n, m = map(int, input().split())
trees = list(map(int,input().split()))

start = 0
end = max(trees)

while start <= end:
    mid = (start+end) // 2
    length = 0
    for i in trees:
        if mid < i:
            length += i - mid
    if length < m:
        end = mid - 1
    else:
        start = mid + 1
print(end)

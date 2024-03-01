import sys

for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    A = sorted(list(map(int, sys.stdin.readline().split())))
    B = list(map(int, sys.stdin.readline().split()))
    answer = 0
    for i in B:
        s = 0
        e = n-1
        while s <= e:
            mid = (s+e) // 2
            if A[mid] > i:
                e = mid - 1
            else:
                s = mid + 1
        answer += (n-s)
    print(answer)
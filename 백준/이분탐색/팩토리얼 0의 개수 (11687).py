import sys

m = int(sys.stdin.readline())

s, e = 1, m*5
answer = -1


def find_right_zeros(n):
    zeros = 0
    while n >= 5:
        zeros += n // 5
        n //= 5
    return zeros


while s <= e:
    mid = (s+e)//2
    
    a = find_right_zeros(mid)
    if a >= m:
        e = mid - 1
        answer = mid
    else:
        s = mid + 1

if find_right_zeros(answer) == m:
    print(answer)
else:
    print(-1)
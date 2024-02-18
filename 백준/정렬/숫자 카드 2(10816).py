import sys

def lower_bound(target):
    start, end = 0, len(card_n)
    while start < end:
        mid = (start + end) // 2
        if card_n[mid] >= target:
            end = mid
        else:
            start = mid + 1
    return start

def upper_bound(target):
    start, end = 0, len(card_n)
    while start < end:
        mid = (start + end) // 2
        if card_n[mid] > target:
            end = mid
        else:
            start = mid + 1
    return start

n = int(sys.stdin.readline().strip())
card_n = sorted(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
card_m = map(int, sys.stdin.readline().strip().split())

for target in card_m:
    lower = lower_bound(target)
    upper = upper_bound(target)
    print(upper - lower, end=" ")
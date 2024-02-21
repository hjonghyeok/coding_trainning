def find_order(n, r, c):
    if n == 0:
        return 0
    half = 2**(n-1)
    if r < half and c < half:  # 1사분면
        return find_order(n-1, r, c)
    if r < half and c >= half:  # 2사분면
        return half**2 + find_order(n-1, r, c-half)
    if r >= half and c < half:  # 3사분면
        return 2*half**2 + find_order(n-1, r-half, c)
    return 3*half**2 + find_order(n-1, r-half, c-half)  # 4사분면

n, r, c = map(int, input().split())
print(find_order(n, r, c))
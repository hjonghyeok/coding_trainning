def rearrange_array(arr):
    n = len(arr)
    # (요소 값 % n, 요소 값)의 튜플로 배열을 변환
    modified_arr = [(val % n, val) for val in arr]
    # 생성된 튜플을 기준으로 배열 정렬
    modified_arr.sort()
    # 정렬된 배열에서 두 번째 요소만 추출하여 새 배열 생성
    result = [val for _, val in modified_arr]
    return result

print(rearrange_array([35, 14, 16, 2, 5, 18, 13]))
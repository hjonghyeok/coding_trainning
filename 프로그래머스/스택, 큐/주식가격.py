def solution(prices):
    length = len(prices)
    answer = [0] * length  # 각 시점에서 가격이 떨어지지 않고 유지되는 시간을 저장할 배열
    stack = []  # 가격이 떨어지지 않은 시점의 인덱스를 저장할 스택

    for i, price in enumerate(prices):
        # 스택이 비어있지 않고 현재 가격이 스택 top의 가격보다 낮은 경우
        while stack and price < prices[stack[-1]]:
            top = stack.pop()
            answer[top] = i - top
        stack.append(i)

    # 스택에 남아 있는 인덱스 처리
    while stack:
        top = stack.pop()
        answer[top] = length - 1 - top

    return answer

print(solution([6,5,4,2,1]))
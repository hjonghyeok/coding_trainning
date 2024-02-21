def solution(tickets):
    tickets.sort(reverse=True)  # 티켓을 역순으로 정렬
    routes = {}  # 출발지별 도착지 목록 저장
    for start, end in tickets:
        if start in routes:
            routes[start].append(end)
        else:
            routes[start] = [end]
    
    stack = ["ICN"]  # DFS를 위한 스택, "ICN"에서 시작
    path = []  # 경로를 저장할 리스트
    while stack:  # 스택이 비어있지 않는 동안
        top = stack[-1]
        # 현재 출발지에서 갈 수 있는 도착지가 있으면 스택에 추가
        if top in routes and routes[top]:
            stack.append(routes[top].pop())
        # 갈 수 있는 도착지가 없으면 경로에 추가
        else:
            path.append(stack.pop())
    return path[::-1]  # 역순으로 반환
print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
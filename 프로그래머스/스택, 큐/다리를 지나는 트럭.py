from collections import deque
from itertools import permutations


def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge_q = deque([0] * bridge_length)
    bridge_weight = 0
    truck_q = deque(truck_weights)
    
    while truck_q or bridge_weight > 0:
        time += 1
        bridge_weight -= bridge_q.popleft()
        
        if truck_q:
            if bridge_weight + truck_q[0] <= weight:
                truck = truck_q.popleft()
                bridge_q.append(truck)
                bridge_weight += truck
            else:
                bridge_q.append(0)
    
    return time

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]	))
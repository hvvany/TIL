# def solution(bridge_length, weight, truck_weights):
#     group_lst = []
#     group = []
#     truck_weights.sort(reverse= True)
#     for i in range(len(truck_weights)):
#         if sum(group) + truck_weights[i] <= weight and len(group) < bridge_length:
#             group.append(truck_weights[i])
#             if i == len(truck_weights) - 1:
#                 group_lst.append(group)
#         else:
#             group_lst.append(group)
#             group = [truck_weights[i]]
#     print(group_lst)
#     print(len(group_lst))
#     answer = len(group_lst)*bridge_length + bridge_length
#     return answer
# print(solution(2,10,[7,4,5,6]))

from collections import deque
def solution(bridge_length, weight, truck_weights):
    on_bridge = deque([0]*bridge_length)
    truck_weights.sort(reverse=True)
    time = 0
    idx = 0
    while truck_weights:
        for idx in range(len(truck_weights)):
            print(f'truck : {truck_weights[idx]}')
            if sum(on_bridge) + truck_weights[idx] <= weight:
                next_truck = truck_weights[idx]
                break
            print(f'next: {next_truck}')
        else:
            next_truck = truck_weights[-1]
        print(f'무게합 : {sum(on_bridge) + next_truck}')
        print(f'다리 위 : {on_bridge}')
        if sum(on_bridge) + next_truck <= weight:
            on_bridge.popleft()
            on_bridge.append(truck_weights.pop(idx))
            print(f'다리 if : {on_bridge}')
        else:
            on_bridge.popleft()
            on_bridge.append(0)
            print(f'다리 else : {on_bridge}')
        time += 1
        print(f'time = {time}\n')
    time += bridge_length
    answer = time
    return answer
print(solution(2, 10, [7, 4, 5, 6]))
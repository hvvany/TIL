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



# -------------------------------------------------------------

# from collections import deque
# def solution(bridge_length, weight, truck_weights):
#     on_bridge = deque([0]*bridge_length)
#     truck_weights = deque(truck_weights)
#     time = 0

#     while truck_weights:
#         if sum(on_bridge) - on_bridge[0] + truck_weights[0] <= weight:
#             on_bridge.popleft()
#             on_bridge.append(truck_weights.popleft())
#         else:
#             on_bridge.popleft()
#             on_bridge.append(0)
#         time += 1
#     time += bridge_length
#     answer = time
#     return answer





from collections import deque
def solution(bridge_length, weight, truck_weights):
    on_bridge = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    time = 0

    sum_bridge = 0
    while truck_weights:
        if sum_bridge - on_bridge[0] + truck_weights[0] <= weight:
            good_bye = on_bridge.popleft()
            new_truck = truck_weights.popleft()
            on_bridge.append(new_truck)
            sum_bridge += new_truck
            sum_bridge -= good_bye
            print(f'다리 if : {on_bridge}')
        else:
            good_bye = on_bridge.popleft()
            on_bridge.append(0)
            sum_bridge -= good_bye
            print(f'다리 else : {on_bridge}')
        time += 1
        print(f'time = {time}\n')
    time += bridge_length
    answer = time
    return answer
print(solution(2, 10, [7, 4, 5, 6]))


# -------------------------------------------------------------


# from collections import deque
# def solution(bridge_length, weight, truck_weights):
#     on_bridge = deque([0]*bridge_length)
#     truck_weights = deque(truck_weights)
#     time = 0
#     light = min(truck_weights)
#     free_pass = weight - light
#     while truck_weights:
#         now_weight = sum(on_bridge) - on_bridge[0]
#         if now_weight == 0:
#             if truck_weights[0] > free_pass:
#                 time += bridge_length
#                 truck_weights.popleft()
#                 continue
#         if now_weight + truck_weights[0] <= weight:
#             on_bridge.popleft()
#             on_bridge.append(truck_weights.popleft())
#             print(f'다리 if : {on_bridge}')
#         else:
#             on_bridge.popleft()
#             on_bridge.append(0)
#             print(f'다리 else : {on_bridge}')
#         time += 1
#         print(f'time = {time}\n')
#     time += bridge_length
#     answer = time
#     return answer
# print(solution(10, 10, [7, 4, 5, 6]))
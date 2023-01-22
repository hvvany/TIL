from itertools import combinations
n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
chicken_lst = []
home_lst = []
result = []

for row in range(n):
    for col in range(n):
        if graph[row][col] == 2:
            chicken_lst.append((row,col))
        elif graph[row][col] == 1:
            home_lst.append((row,col))



numbers_lst = list(combinations(range(len(chicken_lst)),m))
for numbers in numbers_lst:
    answer = 0
    distance_graph = [ [0]*m for _ in range(len(home_lst))]
    for i in range(len(home_lst)):
        idx = 0
        for j in range(len(chicken_lst)):
            if j in numbers:
                r, c = home_lst[i]
                r_, c_ = chicken_lst[j]
                distance_graph[i][idx] = (abs(r-r_) + abs(c-c_))
                idx += 1
        answer += min(distance_graph[i])
    result.append(answer)

print(min(result))

# for i in range(len(chicken_lst)):
#     chick_sum = 0
#     for j in range(len(home_lst)):
#         chick_sum += distance_graph[j][i]
#     answer.append(chick_sum)
# print(answer)



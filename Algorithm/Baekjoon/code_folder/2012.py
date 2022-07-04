# n = int(input())
# num_lst = []
# for _ in range(n):
#   num_lst.append(int(input()))
# num_lst.sort()

# answer = 0
# for i in range(n):
#   answer += abs((i+1)-num_lst[i])
# print(answer)

n = int(input())
ranks = [int(input()) for _ in range(n)]

#초기 등수들을 visited로 두고 모두 0으로 초기화해줌
visited = [0 for _ in range(n+1)]

#등수가 나올때마다
#처음 나온 등수라면, visited를 체크해주고
#이미 나온 등수라면(visited가 체크되어 있으면), left에 담아줌
left = []
for rank in ranks:
    if visited[rank] == 0:
        visited[rank] = 1
    else:
        left.append(rank)

#자신과 가장 이웃한 친구들과 비교해야하니까(순서대로 비교), sort 해줌
left.sort()

#앞에서부터 아직 안나온 등수가 있다면, 
#left의 친구와 차이값을 구해서 total에 더해줌
total = 0
left_temp = 0
for i in range(1, n+1):
    if visited[i] == 0:
        total += (abs((i) - left[left_temp]))
        left_temp += 1

print(total)
n = int(input())
graph = [[0]]+[list(map(int,input().split())) for _ in range(n)]
# print(graph)

answer = []
floor = 2
num_sum = graph[1][0]
def dp(idx):
    global floor, num_sum
    print(f'floor :{floor}')
    for i in range(idx, idx + 2):
        print(f'i : {i}')
        if floor == n:
            answer.append(num_sum + graph[floor][i])
            print(f'answer:{answer}')
            num_sum -= graph[floor][i]
        else:
            if i == n - 1:
                print('no way')
                break
            print(f'floor:{floor}, idx:{i}')
            num_sum += graph[floor][i]
            floor += 1
            dp(i)
    floor -= 1
dp(0)
print(answer)
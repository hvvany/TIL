answer_set = set()
graph = [list(input().split()) for _ in range(5)]

def finder(i,j, answer):
    if len(answer) == 6:
        answer_set.add(answer)
        return
    dx = [-1,0,0,1]
    dy = [0,-1,1,0]
    for idx in range(4):
        x = i + dx[idx]
        y = j + dy[idx]
        if 0 <= x < 5 and 0 <= y < 5:
            finder(x,y, answer + graph[x][y])


for i in range(5):
    for j in range(5):
        cnt = 1
        finder(i,j,graph[i][j])
print(len(answer_set))
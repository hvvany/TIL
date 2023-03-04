import copy, sys
input = sys.stdin.readline

def Permu(cnt):
    if cnt == len(camera_lst):
        DirecSelector(numbers,graph)
        # print(f'numbers : {numbers}')
        return
    for i in range(4):
        numbers[cnt] = i
        Permu(cnt + 1)

def DirecSelector(mode_lst, copy_graph):
    global answer
    first_graph = copy.deepcopy(copy_graph)
    for idx in range(len(mode_lst)):
        mode = mode_lst[idx]
        x = camera_lst[idx][0]
        y = camera_lst[idx][1]
        cam_num = copy_graph[x][y]
        d1 = [1,0,0,0]*2
        d2 = [1,0,1,0]*2
        d3 = [1,1,0,0]*2
        d4 = [1,1,0,1]*2
        d5 = [1,1,1,1]*2
        if cam_num == 1:
            BlackCnt(first_graph,x,y,d1[mode:mode+4])
        elif cam_num == 2:
            BlackCnt(first_graph,x,y,d2[mode:mode+4])
        elif cam_num == 3:
            BlackCnt(first_graph,x,y,d3[mode:mode+4])
        elif cam_num == 4:
            BlackCnt(first_graph,x,y,d4[mode:mode+4])
        elif cam_num == 5:
            BlackCnt(first_graph,x,y,d5[mode:mode+4])
    cnt = 0
    for p in range(N):
        for q in range(M):
            if first_graph[p][q] == 0:
                cnt += 1
    if answer > cnt:
        answer = cnt

def BlackCnt(copy_graph,i,j,direc_lst):
    global N, M
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    for idx in range(4):
        if direc_lst[idx] == 0:
            continue
        nx, ny = i, j
        while True:
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                break
            if copy_graph[nx][ny] == 6:
                break
            copy_graph[nx][ny] = 1
            nx += dx[idx]
            ny += dy[idx]
    return

answer = 10**6
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
camera_lst = []
for i in range(N):
    for j in range(M):
        if graph[i][j] != 0 and graph[i][j] != 6:
            camera_lst.append((i,j))
numbers = [0]*len(camera_lst)
Permu(0)
print(answer)
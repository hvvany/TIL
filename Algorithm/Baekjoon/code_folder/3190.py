# from collections import deque

# n = int(input())
# k = int(input())
# apple = set()
# move = dict()

# for _ in range(k):
#     apple.add(input())  # 문자열 형태로 저장  '3 4', '2 5', ...

# l = int(input())
# for _ in range(l):
#     time, direction = input().split()
#     move[int(time)] = direction

# sec = 0
# idx_right = 0
# idx_down = 0
# move_dir = 'x+'

# while True:
#     # 오른쪽 이동 반복
#     while move_dir == 'x+':
#         if sec in move:
#             if move[sec] == 'D':
#                 move_dir = 'y+'
#             else:
#                 move_dir = 'y-'



from collections import deque

n = int(input())
k = int(input())

graph = [[0] * n for _ in range(n)]

for i in range(k):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 2

l = int(input())


dir_dic = dict()
queue = deque()
queue.append((0, 0))

for i in range(l):
    x, c = input().split()
    dir_dic[int(x)] = c

x, y = 0, 0
graph[x][y] = 1
cnt = 0
direction = 0

def turn(alpha):
    global direction
    if alpha == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while True:
    cnt += 1
    x += dx[direction]
    y += dy[direction]

    if x < 0 or x >= n or y < 0 or y >= n:
        break

    if graph[x][y] == 2:
        graph[x][y] = 1
        queue.append((x, y))
        if cnt in dir_dic:
            turn(dir_dic[cnt])

    elif graph[x][y] == 0:
        graph[x][y] = 1
        queue.append((x, y))
        tx, ty = queue.popleft()
        graph[tx][ty] = 0
        if cnt in dir_dic:
            turn(dir_dic[cnt])

    else:
        break

print(cnt)
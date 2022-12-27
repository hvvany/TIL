import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m, k, x = map(int,input().split())
connection = [[] for _ in range(n+1)]
visited = [False]*(n+1)
depth = 0
answer = set()
result = []

# 연결 상태 입력받아서 connection에 추가
for _ in range(m):
    idx, number = map(int,input().split())
    connection[idx].append(number)

# 함수 선언
def dfs(num_lst):
    global depth
    depth += 1  # 깊이 레벨 저장
    if depth == k:   # 깊이가 목표치에 도달하면
        for num in num_lst:   # 입력 받은리스트 숫자 모두 추가
            visited[num] = True
            answer.add(num)
    else:            # 깊이가 목표치와 다르면
        next_lst = set()
        for number in num_lst:
            if visited[number] == False:  # 방문 안한 숫자이면
                visited[number] = True    # 방문 처리 후
                for num in connection[number]:
                    next_lst.add(num)     # next_lst에 저장
        dfs(next_lst)                     # 재귀 호출

visited[x] = True   # 본인 최단거리는 0이므로 방문처리
dfs(connection[x])  # 함수 호출
if len(answer) > 0:    # answer가 비어있지 않으면
    for number in answer:
        if visited[number] == False:
            result.append(number)
    result.sort()      # 정렬
    for num in result: #
        print(num)
else:
    print(-1)
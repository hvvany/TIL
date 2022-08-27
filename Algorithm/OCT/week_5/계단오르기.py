n = int(input())
point_lst = [0,0]
score_lst = []
for _ in range(n):
  point_lst.append(int(input()))
point_lst.reverse()
print(point_lst)

score_lst.append(point_lst[0])   # 마지막 계단은 무조건 밟아야 한다. i = 0인 위치에서 시작
i = 1
stair_stack = 1
while i < n:
  if stair_stack == 1:                  # 한 칸만 먹고 있는 상태에서는 두 가지 선택 가능
    if point_lst[i] > point_lst[i+1]:   # 바로 다음 칸이 더 크면
      score_lst.append(point_lst[i])
      stair_stack += 1
      i += 1
      print(f'1i : {i}')
      print(f'1stair_stack : {stair_stack}')
      print(f'1score_lst : {score_lst}')
    elif point_lst[i] < point_lst[i+1]:  # 건너 칸이 더 크면
      score_lst.append(point_lst[i+1])
      i += 2
      print(f'2i : {i}')
      print(f'2stair_stack : {stair_stack}')
      print(f'2score_lst : {score_lst}')
    else:
      score_lst.append(point_lst[i+1])   # 같은 경우는 어차피 둘 중 하나 선택이여서 넓은 선택지 위해 다음 수 선택
      i += 2
      print(f'3i : {i}')
      print(f'3stair_stack : {stair_stack}')
      print(f'3score_lst : {score_lst}')
  elif stair_stack == 2:                 # 바로 다음칸 선택 불가능. 한 가지 경우만 존재
    score_lst.append(point_lst[i+1])
    stair_stack = 1
    i += 2
    print(f'4i : {i}')
    print(f'4stair_stack : {stair_stack}')
    print(f'4score_lst : {score_lst}')

print(sum(score_lst))
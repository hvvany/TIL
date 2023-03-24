import heapq, sys
input = sys.stdin.readline

T = int(input())
for test_case in range(T):
  lst_big = []
  lst_small = []
  check_dic = dict()
  N = int(input())
  cnt = 0
  for _ in range(N):
    cal, num = input().split()
    if cal == 'I':
      cnt += 1
      if int(num) in check_dic:
        check_dic[int(num)] += 1
      else:
        check_dic[int(num)] = 1
      heapq.heappush(lst_big,-int(num))
      heapq.heappush(lst_small,int(num))
    else:
      if cnt == 0:
        continue
      if num == '1':
        while True:
          check_num = -heapq.heappop(lst_big)
          if check_dic[check_num] != 0:
            check_dic[check_num] -= 1
            cnt -= 1
            break
      else:
        while True:
          check_num = heapq.heappop(lst_small)
          if check_dic[check_num] != 0:
            check_dic[check_num] -= 1
            cnt -= 1
            break
  if cnt == 0:
    print('EMPTY')
  else:
    while True:
          check_num = -heapq.heappop(lst_big)
          if check_dic[check_num] != 0:
            print(check_num, end=' ')
            break
    while True:
          check_num = heapq.heappop(lst_small)
          if check_dic[check_num] != 0:
            print(check_num)
            break
def solution(cap, n, deliveries, pickups):
    deliv_lst = []
    pick_lst = []
    cnt = 0

    for i in range(len(deliveries)):
      if deliveries[i] != 0:
        deliv_lst += [i+1]*deliveries[i]
    for j in range(len(pickups)):
      if pickups[j] != 0:
        pick_lst += [j+1]*pickups[j]

    for idx in range(1,max(len(deliv_lst),len(pick_lst))+1,cap):
      if idx <= len(deliv_lst):
        num_deliv = deliv_lst[-idx]
      else:
        num_deliv = 0
      if idx <= len(pick_lst):
        num_pick = pick_lst[-idx]
      else:
        num_pick = 0
      cnt += max(num_deliv, num_pick)*2

    return cnt

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))






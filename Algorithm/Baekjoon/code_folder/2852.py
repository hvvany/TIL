# n = int(input())
# input_lst = []
# for _ in range(n):
#     input_lst.append(input())

# score_lst = [0]*2
# last_win = 48*60  # 48분 부터 거꾸로
# before_winner = '0'
# before_time = 0
# for team, time in input_lst[::-1]:
#     time = int(time[:2])*60 + int(time[3:])
#     if team == '1':
#         if before_winner == '2':
#             winner_lst[2] += last_win - before_time
#             last_win = time
#         else:
#             winner_lst[1]
#         before_winner = '1'
#     else:
#         if before_winner == '1':
#             winner_lst[1] += last_win - before_time
#             last_win = time
#         before_winner = '2'
#     before_time = time

# for team in winner_lst[1:]:
#     minute = team//60
#     second = team%60
#     if minute < 10:
#         if minute == 0:
#             minute = '00'
#         else:
#             minute = '0' + str(minute)
#     if second < 10:
#         if second == 0:
#             second = '00'
#         else:
#             second = '0' + str(second)
#     print(f'{minute}:{second}')
# before_team = ''
# before_time = 0

# for i in range(n):
#     team, time = input_lst[i].split()
#     time = int(time[:2])*60 + int(time[3:])
#     if i == 0:
#         before_time = time
#         before_team = team
#     elif i == n-1:
#             if team != before_team:
#                 score_lst[int(team)-2] += time - before_time
#                 score_lst[int(team)-1] += 48*60 - time
#             else:
#                 score_lst[int(team)-1] += 48*60 - before_time
#     else:
#         if team != before_team:
#             score_lst[int(team)-2] += time - before_time
#             before_team = team
#             before_time = time

# for t in score_lst:
#     minute = t//60
#     second = t%60
#     if minute < 10:
#         if minute == 0:
#             minute = '00'
#         else:
#             minute = '0' + str(minute)
#     if second < 10:
#         if second == 0:
#             second = '00'
#         else:
#             second = '0' + str(second)
#     print(f'{minute}:{second}')
winner_time = []
n = int(input())
winner = ''
first_winner = ''
for i in range(n):
    team, time = input().split()
    if not winner_time:
        first_winner = team
        winner = team
        winner_time.append(time)
    elif team != winner:
        winner_time.append(time)
        winner = team
winner_time.append('48:00')
answer = [0]*2
print(winner_time)
for i in range(len(winner_time)-1):
    time = (int(winner_time[i+1][:2])*60 + int(winner_time[i+1][3:])) - (int(winner_time[i][:2])*60 + int(winner_time[i][3:]))
    answer[int(first_winner)-1] += time
    first_winner = 3-int(first_winner)
print(answer)
for t in answer:
    minute = t//60
    second = t%60
    if minute < 10:
        if minute == 0:
            minute = '00'
        else:
            minute = '0' + str(minute)
    if second < 10:
        if second == 0:
            second = '00'
        else:
            second = '0' + str(second)
    print(f'{minute}:{second}')
# def solution(genres, plays):
#   genres_dic = dict()
#   genres_sort_lst = []
#   id_dic = dict()
#   answer = []

#   for i in range(len(genres)):     # genres_dic 재생수 추가 및 id_dic추가
#     if genres[i] in genres_dic:
#       if genres_dic[genres[i]][-1] < plays[i]:
#         id_dic[genres[i]].insert(0,i)
#         id_dic[genres[i]].pop()
#       elif genres_dic[genres[i]][-1] == plays[i]:
#         if genres_dic[genres[i]][-2] == plays[i]:
#           pass
#         else:
#           id_dic[genres[i]].pop()
#           id_dic[genres[i]].append(i)
#       genres_dic[genres[i]] += [plays[i]]
#     else:
#       genres_dic[genres[i]] = [0,plays[i]]
#       id_dic[genres[i]] = [i,-1]        
#   print(f'genres_dic : {genres_dic}')
#   print(f'id_dic : {id_dic}')

#   for genre in genres_dic:   # genres_dic 리스트 대신 합계 숫자로
#     genres_dic[genre] = sum(genres_dic[genre])
#   print(f'정렬한 genres_dic : {genres_dic}')

#   while genres_dic:
#     play_max = 0
#     play_max_genre = 0
#     print(f'for문 내부 genres_dic : {genres_dic}')
#     for genre in genres_dic:
#       if genres_dic[genre] > play_max:
#         play_max_genre = genre
#         play_max = genres_dic[genre]
#         print(f'play_max_genre : {play_max_genre}')
#     genres_sort_lst.append(play_max_genre)
#     genres_dic.pop(play_max_genre)

#   for genre in genres_sort_lst:
#     for id in id_dic[genre]:
#       if id >= 0:
#         answer.append(id)
#   print(f'answer : {answer}')

#   return answer

# genres = ["classic", "pop", "classic", "classic", "pop", 'classic', 'classic', 'classic']
# plays = [500, 600, 150, 800, 2500, 300, 300, 300]
# solution(genres, plays)




def solution(genres, plays):
  genres_dic = dict()            # {'classic': [500, 150, 800], 'pop': [600, 2500]}
  genres_sort = dict()           # {'classic': [800, 500, 150], 'pop': [2500, 600]}
  genres_sum = dict()            # {'classic': 1450, 'pop': 3100}
  genres_list = []               # ['pop', 'classic']
  answer = []                    # [4, 1, 3, 0]

  # genres_dic 만들기 _ {'classic': [500, 150, 800], 'pop': [600, 2500]}
  for i in range(len(genres)):               
    if genres[i] in genres_dic:
      genres_dic[genres[i]] += [plays[i]]    # 이미 존재하는 장르
    else:
      genres_dic[genres[i]] = [plays[i]]     # 처음 들어온 장르


  # genres_sort 만들기 _ {'classic': [800, 500, 150], 'pop': [2500, 600]}
  for genre in genres_dic:
    genres_sort[genre] = sorted(genres_dic[genre],reverse=True)  # 장르 값을 큰 순서대로 genres_sort에 정렬 추가


  # genres_sum 만들기 _ {'classic': 1450, 'pop': 3100}
  for genre in genres_dic:
    genres_sum[genre] = sum(genres_dic[genre])


  # genres_list 만들기
  while genres_sum:       # 장르 합계로 내림차순으로 genres_list에 추가 후 pop
    play_max = 0          # 최대 재생 수 최신화 기록
    play_max_genre = 0    # 최대 재생 장르 최신화 기록

    for genre in genres_sum:
      if genres_sum[genre] > play_max:    # for문을 돌며 최대 재생수 장르 최신화
        play_max_genre = genre
        play_max = genres_sum[genre]

    genres_list.append(play_max_genre)    # 최대 재생수 장르 genres_list 추가
    genres_sum.pop(play_max_genre)        # 기록한 데이터는 삭제 pop


  # answer 만들기
  for genre in genres_list:                # 장르 재생 수 많은 장르부터 가져옴
    music_cnt = len(genres_dic[genre])     # 장르에 저장되어 있는 노래 수

    if music_cnt >= 2:                     # 2곡 이상 저장되어 있는 경우 앨범 고유 번호 2개 answer 추가
      for idx in range(len(plays)):
        if plays[idx] == genres_sort[genre][0] and genres[idx] == genre:
          plays[idx] = 0
          answer.append(idx)
          break
      for idx in range(len(plays)):
        if plays[idx] == genres_sort[genre][1] and genres[idx] == genre:
          plays[idx] = 0
          answer.append(idx)
          break

    elif music_cnt == 1:                   # 1곡만 저장되어 있는 경우 앨범 고유 번호 1개 answer 추가
      for idx in range(len(plays)):
        if plays[idx] == genres_sort[genre][0] and genres[idx] == genre:
          plays[idx] = 0
          answer.append(idx)
          break

  return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

# genres = ["classic", "pop", "classic", "classic", "pop", 'balad']
# plays = [500, 600, 150, 800, 2500, 300]

# genres = ["classic", "pop", "classic", "classic", "pop", 'balad', 'balad']
# plays = [500, 600, 150, 800, 2500, 300, 300]

print(solution(genres, plays))








# 다른 사람 풀이
# def solution(genres, plays):
#     answer = []
#     dic = {}
#     album_list = []
#     for i in range(len(genres)):
#         dic[genres[i]] = dic.get(genres[i], 0) + plays[i]
#         album_list.append(album(genres[i], plays[i], i))

#     dic = sorted(dic.items(), key=lambda dic:dic[1], reverse=True)
#     album_list = sorted(album_list, reverse=True)



#     while len(dic) > 0:
#         play_genre = dic.pop(0)
#         print(play_genre)
#         cnt = 0;
#         for ab in album_list:
#             if play_genre[0] == ab.genre:
#                 answer.append(ab.track)
#                 cnt += 1
#             if cnt == 2:
#                 break

#     return answer

# class album:
#     def __init__(self, genre, play, track):
#         self.genre = genre
#         self.play = play
#         self.track = track

#     def __lt__(self, other):
#         return self.play < other.play
#     def __le__(self, other):
#         return self.play <= other.play
#     def __gt__(self, other):
#         return self.play > other.play
#     def __ge__(self, other):
#         return self.play >= other.play
#     def __eq__(self, other):
#         return self.play == other.play
#     def __ne__(self, other):
#         return self.play != other.play
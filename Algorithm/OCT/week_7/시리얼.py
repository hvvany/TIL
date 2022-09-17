# 길이 짧은 것 먼저
# 숫자인 것만 더해서 작은 수  먼저
# 사전순
n = int(input())

serial_dic = dict()
for _ in range(n):
  serial_dic[input()] = []

# 첫 번째 기준. 길이 저장
for k in serial_dic:
  serial_dic[k].append(len(k))

# 두 번째 기준. 숫자 합 저장
for k in serial_dic:
  cnt = 0
  for text in k:
    if text in '1234567890':
      cnt += int(text)
  serial_dic[k].append(cnt)

# 세 번째 기준. 사전순
for k in serial_dic:
  serial_dic[k].append(k)

# 결과
sort_lst = []
for k in serial_dic:
  sort_lst.append(serial_dic[k])
sort_lst.sort()

for value in sort_lst:
  for k in serial_dic:
    if serial_dic[k] == value:
      print(k)
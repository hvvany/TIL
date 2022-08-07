import time
phone_lst = []
phone_number = ''
for number in range(1000):
    if len(phone_lst) == 10000:
        break
    phone_number += str(number)
    phone_lst.append(phone_number)
    
print(phone_lst)



# 처음 구현한 코드 => 효율성 시간 초과
def solution(phone_book):                              # 리스트 형태의 전화 번호 목록 받음
    cnt = 0                                            # 중복 횟수 기록 위한 초기값
    for number_1 in phone_book:                        # 전화번호부에서 하나씩 가져오기
        for number_2 in phone_book:                    # 비교할 전화번호 하나씩 가져오기
            if number_1 == number_2[0:len(number_1)]:  # 첫 번째 번호 길이의 숫자 같은게 두 번째 왼쪽에 있는지
                cnt += 1                               # 같으면 접두사 번호이므로 카운트 추가
            if cnt > len(phone_book):                  # 자기 자신 카운트보다 크면 접두사 번호 존재
                answer = False                         # 존재하면 false 전달
            else:                                      # 존재하지 않으면
                answer = True                          # True 전달
    return answer
start_time = time.time()
solution(phone_lst)
finish_time = time.time()
efficiency = finish_time - start_time
print(f'개선전 : {efficiency}')
#--------------------------------------------------------------------------------------------------

# 효율성 개선 코드
def solution(phone_book):                             # 리스트 형태의 전화 번호 목록 받음
    phone_book.sort()                                 # 전화번호부 숫자 순서대로 정렬
    answer = True                                     # 기본값으로 True 전달
    for i in range(len(phone_book)-1):                # 리스트에서 하나씩 가져와서 인덱스 접근
        if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]: # 위와 같은 방식으로 바로 옆에것만 비교해본다.
            answer = False                            # 만약 같으면 false 전달
            return answer                             # false이면 더이상 비교할 필요 없으므로 return후 종료
    return answer                                     # true일때 return True
start_time = time.time()
solution(phone_lst)
finish_time = time.time()
efficiency = finish_time - start_time
print(f'개선후 : {efficiency}')
# sort로 정렬한 후 옆에것만 비교하는 방식을 알면 정말 쉬운 문제인데 
# 처음 보면 효율성 0점 결과에 당황하게되는 문제
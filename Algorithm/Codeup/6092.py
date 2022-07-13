# 정보 선생님은 수업을 시작하기 전에 이상한 출석을 부른다.

# 선생님은 출석부를 보고 번호를 부르는데,
# 학생들의 얼굴과 이름을 빨리 익히기 위해 번호를 무작위(랜덤)으로 부른다.

# 그리고 얼굴과 이름이 잘 기억되지 않는 학생들은 번호를 여러 번 불러
# 이름과 얼굴을 빨리 익히려고 하는 것이다.

# 출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자.

# 예시
# n = int(input())      #개수를 입력받아 n에 정수로 저장
# a = input().split()  #공백을 기준으로 잘라 a에 순서대로 저장

# for i in range(n) :  #0부터 n-1까지...
#   a[i] = int(a[i])       #a에 순서대로 저장되어있는 각 값을 정수로 변환해 다시 저장

# d = []                     #d라는 이름의 빈 리스트 [ ] 변수를 만듦. 대괄호 기호 [  ] 를 사용한다.
# for i in range(24) :  #[0, 0, 0, ... , 0, 0, 0] 과 같이 24개의 정수 값 0을 추가해 넣음
#   d.append(0)        #각 값은 d[0], d[1], d[2], ... , d[22], d[23] 으로 값을 읽고 저장할 수 있음.

# for i in range(n) :    #번호를 부를 때마다, 그 번호에 대한 카운트 1씩 증가
#   d[a[i]] += 1

# for i in range(1, 24) :  #카운트한 값을 공백을 두고 출력
#   print(d[i], end=' ')

total = int(input())
lst = list(map(int,input().split()))
count_lst = []
for i in range(23):
    count_lst.append(0)
for student_num in lst:
    count_lst[student_num-1] += 1
for t in count_lst:
    print(t, end=' ')
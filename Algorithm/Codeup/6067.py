# 0이 아닌 정수 1개가 입력되었을 때, 음(-)/양(+)과 짝(even)/홀(odd)을 구분해 분류해보자.
# 음수이면서 짝수이면, A
# 음수이면서 홀수이면, B
# 양수이면서 짝수이면, C
# 양수이면서 홀수이면, D
# 를 출력한다.

# 예시
# ...
# if n<0 :
#   if n%2==0 :
#     print('A')      #주의 : 변수 A와 문자열 'A' / "A" 는 의미가 완전히 다르다. 
#   else :
#     print('B')
# else :
#   if n%2==0 :
#     print('C')
#   else :
#     print('D')
# ...

a = input()
a = int(a)

if a<0 :
  if a%2==0 :
    print('A')     
  else :
    print('B')
else :
  if a%2==0 :
    print('C')
  else :
    print('D')


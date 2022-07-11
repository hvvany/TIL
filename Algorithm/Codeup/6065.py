# 3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.

# 예시
# a, b, c = input().split()

# a = int(a)
# b = int(b)
# c = int(c)

# if a%2==0 :  #논리적으로 한 단위로 처리해야하는 경우 콜론(:)을 찍고, 들여쓰기로 작성 한다.
#   print(a)

# if b%2==0 :
#   print(b) 

# if c%2==0 :
#   print(c) 

a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if a%2==0 :  #논리적으로 한 단위로 처리해야하는 경우 콜론(:)을 찍고, 들여쓰기로 작성 한다.
  print(a)

if b%2==0 :
  print(b) 

if c%2==0 :
  print(c) 
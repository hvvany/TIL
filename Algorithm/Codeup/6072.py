# 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

# while 조건식 :
#   ...
#   ...
# 반복 실행구조를 사용해 보자.

# 예시
# ...
# while n!=0 :
#   print(n)
#   n = n-1
# ...

n = int(input())
a = n
count = 0
while count < n:
    print(a)
    a -= 1
    count += 1

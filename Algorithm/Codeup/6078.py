# 영문 소문자 'q'가 입력될 때까지
# 입력한 문자를 계속 출력하는 프로그램을 작성해보자.


text = ord('p')

while text != ord('q'):
    text = ord(input())
    print(chr(text))
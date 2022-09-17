# 인풋을 문자열로 받기
# 스트립 해서 공백 제거
# 순회하며 리스트에 [개수, 문자] 담기
# sort하기  -> 숫자 기준 그다음 문자 기준 정렬
# 뒤에서 부터 접근해서 마지막 숫자와 달라지는 인덱스 찾아서 그 다음 인덱스 부터 마지막 까지 문자 출력
import sys
input = sys.stdin.read

text = input()
print(text)
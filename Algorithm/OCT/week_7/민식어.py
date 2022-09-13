minsik = list(' a b k d e g h i l m n ng o p r s t u w y'.split())
# n 이면 ng인지 확인
# k와 ng 말고는 그대로이다.
# c 대신 k , ng 대신 nz 로 두면 된다.

n = int(input())
word_lst = []
new_word_lst = []
for _ in range(n):
  word_lst.append(input())

for word in word_lst:
  new_word = word.replace('k','c')
  new_word_2 = new_word.replace('ng','nz')
  new_word_lst.append(new_word_2)

for word in sorted(new_word_lst):
  answer = word.replace('c','k')
  answer_2 = answer.replace('nz','ng')
  print(answer_2)
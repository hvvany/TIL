# 프로젝트 코드리뷰

#코드리뷰 #hphk #파이썬



## <프로젝트 4 리뷰>

1. ## 민석이의 과제 체크하기

   > **첨삭 부분 코드**

   ```python
   submit_lst = list(map(int,input().split()))
   for num in submit_lst:
       submit_set.add(num)
   ```

   > **첨삭 내용**

   리스트로 입력을 받아 값들을 하나하나 `set`에 넣기보다는 애초에 `submit_set = set(map(int,input().split()))` 으로 바로 받는건 어떨까요?

   > **느낀점**

   맞다. list( ) 또는 set( )같은 메서드는 arguments를 하나만 받을 수 있어서 리스트로 먼저 바꾸고 리스트 하나만 넣어줘야 한다고 생각했는데 리스트도 map 을 쓰면 입력을 한 번에 받을 수 있으므로 set도 가능하다!!

   

   

2. ## 괄호짝짓기

   > **첨삭 부분 코드**

   ```python
   if small_g != 0 or middle_g != 0 or big_g != 0 or angle_g != 0:
           result = 0
       print(f'#{test+1} {result}')
   ```

   > **첨삭 내용**

   다음과 같은 입력이 들어온다면 어떤 결과를 출력해야 할까요?

   ```
   4
   <(>)
   ```

   이 문제에서는 영향이 없지만 같은 유형의 다른 문제를 만나시게 된다면 위와 같은 테스트케이스를 어떻게 처리하는냐가 영향을 미칠 수 있기 때문에 한번 고민해보시기를 추천드립니다.

   > **느낀점**

   먼저 코드가 어땠는지 전체를 봐야 알것 같다.

   ```python
   # import sys
   
   # sys.stdin = open("_괄호짝짓기.txt")
   
   t = 10
   for test in range(t):
       long = int(input())
       gual = input()
       small_g, middle_g, big_g, angle_g = 0, 0, 0, 0
       result = 1
       for text in gual:
           if text == '(':
               small_g += 1
           elif text == '[':
               middle_g += 1
           elif text == '{':
               big_g += 1
           elif text == '<':
               angle_g += 1
           elif text == ')':
               small_g -= 1
           elif text == ']':
               middle_g -= 1
           elif text == '}':
               big_g -= 1
           elif text == '>':
               angle_g -= 1
           if small_g < 0 or middle_g < 0 or big_g < 0 or angle_g < 0:
               result = 0
               break
       if small_g != 0 or middle_g != 0 or big_g != 0 or angle_g != 0:
           result = 0
       print(f'#{test+1} {result}')
   ```

   원래 이런 괄호 문제를 풀때 리스트로 접근하여 두 인덱스 범위를 통해  '<>(){}[]' 에 해당하는 문자가 있으면 해당 인덱스에 접근하여 pop을 두번 해줬다. 이 문제는 괄호를 위에 예외를 적어 주신 것 처럼 주는 경우가 없어서 통과를 하였다. 귀찮아도 기존의 방법대로 전체 입력을 리스트로 받아서 pop을 두번 해주는 것이 확실할 것 같다.

   위의 방식으로 이전에 통과한 적이 있는 문제가 있는데 백준에서 한 가지 종류의 괄호만 나왔을 경우이다. 위 문제처럼 4가지가 썪여있지 않아 위의 접근 방식대로 접근하면 예외를 모두 파악할 수 있다. 

   한 가지 괄호 => 위의 방식대로 간단한 방식으로 가능

   여러 종류의 괄호 => 리스트에 담아서 pop 두 번 하는 방식으로 줄여 가자

   

   

## <프로젝트3 리뷰>

1. ## 신용카드만들기2

   > **첨삭 부분 코드**

   ```python
   t = int(input())                                            # 케이스 개수
   
   for i in range(t):                                          # 케이스 반복
       number_lst = list(map(str, input()))
   ```

   > **첨삭 내용**

   `input()`은 기본적으로 입력된 값을 문자열로 저장합니다. 따라서 굳이 `map` 함수를 써서 문자열로 변환하지 않아도 `list(input())`으로 저장하면 데이터가 문자열로 저장됩니다!

   > **느낀점**

   맞다. 얼마전에 강사님이 강요해주셔서 기억이 난다. 초반에는 문자열을 어떻게 한 글자씩 리스트에 담을지가 큰 고민이었다. 연구해본 결과 형 변환을 하고 map으로 리스트에 담으니 하나씩 담겼다. 그런데 그냥 list(input()) 이렇게 사용하면 알아서 입력에 공백이 없어도 하나씩 리스트에 담겼다.

# Python 조건문/반복문



## 제어문

- 파이썬은 위에서 이래로 순차적으로 명령 수행
- 특정 상황에 따라 선택적으로 분기, 반복하는 제어가 필요
- 제어문은 순서도로 표현이 가능



## 조건문

### 조건문 기본

- 조건문은 참/거짓을 판단할 수 있는 조건식과 함께 사용

- 기본 형식

  ```python
  if <expression>:
      # Run this Code Block
  else:
      # Run this Code Block     -> else는 생략 가능
  ```

- 예제

  ```python
  # 조건문을 통해 변수 num의 홀수/짝수 여부를 출력하시오.
  num = int(input())
  if num % 2 == 1:
      print('홀')
  else:
      print('짝')
  ```

  

### 복수 조건문

- 복수의 조건식을 활용할 경우 elif를 활용하여 표현

  ```python
  if <expression>:
      # Code Block
  elif <expression>:
      # Code Block
  else :
      # Code Block
  ```

- 예제

  ```python
  # dust 값에 따라 미세먼지 등급을 출력하는 조건식을 작성하시오.
  dust = 80
  
  if dust > 150 :
      print('매우 나쁨')
  elif dust > 80 :
      print('나쁨')
  elif dust > 30 :
      print('보통')
  else:
      print('좋음')
  print('미세먼지 확인 완료')
  ```

### 	

### 중첩 조건문

- 조건문은 다른 조건문에 중첩되어 사용될 수 있음

  > #### 들여쓰기 주의!!! 파이썬에서는 들여쓰기로 구문 범위 인식하므로 중요!!

  ```python
  if <expression>:
      # Code Block
      if <expression>:
          # Code Block
  else:
      # Code Block
  ```



### 조건 표현식

- 조건 표현식을 일반적으로 조건에 따라 값을 할당 할 때 활용

  ```python
  <true인 경우 값> if <expression> else <false인 경우 값>
  ```







## 반복문

- 특정 조건을 도달할 때까지, 계속 반복되는 일련의 문장



### 반복문의 종류

- ### while문

  - `종료 조건`에 해당하는 코드를 통해 반복문을 종료시켜야함

- #### for문

  - 반복 가능한 객체를 모두 순회하면 종료 (`별도의 종료 조건이 필요 없음`)

- #### 반복 제어

  - break, continue, for-else



### While 문

- while문은 조건식이 참인 경우 반복적으로 코드를 실행. 거짓이 되면 탈출

  - 조건이 참인 경우 들여쓰기 코드 블록 실행

  - 코드 블록 실행 후 다시 조건 비교후 재실행

  - 무한 루프 돌지 않게 종료 조건 필요

    ```python
    while <expression>:
        # Code Block
    ```

  - 예제

    ```python
    # 1부터 사용자가 입력한 양의 정수까지의 총합을 구하는 코드를 작성하시오.
    
    # 값 초기화
    n = 0
    total = 0
    user_input = int(input())
    
    while n <= user_input:
        total += n
        n += 1
    print(total)
    ```



### For 문

- for문은 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체 요소를 모두 순회함

  ```python
  for <변수명> in <iterable> :
      # Code Block
  ```

- For문의 일반 형식

  - Iterable

    - 순회할 수 있는 자료형

      > str, list, dict 등

    - 순회형 함수

      > range, enumerate

- 예제

  ```python
  # 문자열 순회
  chars = input()  # hi 입력
  for i in range(len(chars)):
      print(chars[i])
  # h
  # i
  
  
  # enumerate 순회
  인덱스와 객체를 쌍으로 담은 열거형 객체 반환
  
  members = ['민수', '영희', '철수']
  
  for i in range(len(members)):
      print(f'{i} {members[i]}')
      
  for i, member in enumerate(members):
      print(i, member)
      
      
  # dictionary 순회
  딕셔너리는 기본적으로 key를 순회하며, key를 통해 값을 활용
  grades = {'john' : 80, 'eric' : 90}
  for name in grades:
      print(name)
  # john
  # eric
  
  grades = {'john' : 80, 'eric' : 90}
  for name in grades:
      print(name, grades[name])
  # john 80
  # eric 90
  ```

  

### 반복문 제어

- #### break

  - 반복문을 종료

- #### continue

  - continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행

- #### for-else

  - 끝까지 반복문을 실행한 이후에 else문 실행
    - break를 통해 중간에 종료되는 경우 else 문은 실행되지 않음

#### **break**

- break문을 만나면 반복문은 종료됨

  ```python
  n = 0
  while True:
      if n == 3:
          break
      print(n)
      n += 1
  # 0 1 2
  
  for i in range(10):
      if i > 1:
          print('0과 1만 필요해!')
          break
      print(i)
  # 0 1 0과 1만 필요해!
  ```

  

#### continue

- continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행

  ```python
  for i in range(6):
      if i % 2 == 0:
          continue
      print(i)
  # 1 3 5
  ```

  

#### for-else

- else문은 break로 중단되었는지 여부에 따라 실행

  ```python
  for char in 'apple':
      if char == 'b':
          print('b!')
          break
  else:
      print('b가 없습니다.')
  # b가 없습니다.
  
  
  for char in 'banana':
      if char == 'b':
          print('b!')
          break
  else:
      print('b가 없습니다.')
  # b!
  ```

  








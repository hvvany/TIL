# 파이썬 응용

#comprehension #lambda #filter #pip



## 추가문법

### comprehension

- List Comprehension

  > 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법
  >
  > **[ \<expression> `for` <변수> `in` \<iterable> `if` <조건식> ]**

  ```python
  cubic_list = []
  for number in range(1, 4):
  cubic_list.append(number**3)
  print(cubic_list)
  ```

  ```python
  [number**3 for number in range(1, 4)]
  ```

  > 4줄의 코드가 한 줄로!

  

- Dictionary Comprehension

  > 표현식과 제어문을 통해 특정한 값을 가진 딕셔너리를 간결하게 생성하는 방법
  >
  > **{ key : value for <변수> in \<iterable> if <조건식> }**

  ```python
  cubic_dict = {}
  for number in range(1, 4):
  cubic_dict[number] = number ** 3
  print(cubic_dict)
  ```

  ```python
  {number: number**3 for number in range(1, 4)}
  ```



### lambda

> **"임시 생성 함수"**
>
> **lambda [parameter] : 표현식**
>
> lambda n : n*4   #예시

- 람다함수
  - 표현식을 계산한 결과값을 반환하는 함수로, 이름이 없는 함수여서 익명함수라고도 불림
- 특징
  - return문을 가질 수 없음
  - 간편 조건문 외 조건문이나 반복문을 가질 수 없음
- 장점
  - 함수를 정의해서 사용하는 것 보다 간결하게 사용 가능
  - def를 사용할 수 없는 곳에서도 사용가능

- 예시

  ```python
  # map(함수, 반복가능한 것)
  # 반복 가능한 것들의 모든 요소에 함수를 적용시킨 결과를 
  # map object로 반환한다~!
  
  # map(int, input().split())
  # int 형 변환함수를 
  # input으로 받은 것을 쪼갠 결과인 리스트에 각각 적용한다. 
  
  numbers = [1, 2, 5, 10, 3, 9, 12]
  
  # 기본 반복/조건 코드
  result = []
  for n in numbers:
      result.append(n*3)
  print(result)
  
  # 만약에 map으로 쓰고 싶다면?
  # 함수를 정의하셔야 합니다. 
  
  def multiple_3(n):
      return n * 3
  
  print(list(map(multiple_3, numbers)))
  
  # 이 함수는 계속 사용되지 않고, map에서만 사용된다.
  # 임시적인 함수를 만들고 싶다. => lambda
  
  print(list(map(lambda n: n*3, numbers)))
  ```

  

### filter

> 함수를 모든 iterable요소에 적용하고 True이면 반환
>
> **filter( function, iterable )**

- 예시

  ```python
  # 3의 배수인 리스트로만 만들기
  
  numbers = [1, 2, 5, 10, 3, 9, 12]
  
  # 기본 반복/조건 코드
  result = []
  for n in numbers:
      if n % 3 == 0:
          result.append(n)
  print(result)
  
  # 람다 활용
  print(list(filter(lambda n: n%3==0, numbers)))
  
  # 함수 활용
  def is_3(n):
      return n % 3 == 0
  print(list(filter(is_3, numbers)))
  
  # def is_3_1(n):
  #     if n % 3 == 0:
  #         return True 
  #     else: 
  #         return False





## 파이썬 버전별 업데이트

### PSL (Python Standard Library)

- 파이썬에 기본적으로 설치된 모듈과 내장 함수

### PIP (파이썬 패키지 관리자)

- 명령어

  ```python
  $ pip install SomePackage
  ```



## 가상 환경

- 파이썬 표준 라이브러리가 아닌 **외부 패키지와 모듈**을 사용하는 경우 모두 pip를 통해 설치를 해야함
- 복수의 프로젝트를 하는 경우 **버전이 상이**할 수 있음
- 이러한 경우 가상환경을 만들어 **프로젝트별로 독립적인 패키지를 관리** 할 수 있음

### 파이썬 실행

- 파이썬은 특정 경로에 있는 프로그램을 실행시키는 것

  ```python
  C:// ~~~/Python
  ```

### venv

- 가상 환경을 만들고 관리하는데 사용되는 모듈 (Python 3.5 이상부터)
- 특정 디렉토리에 가상 환경을 만들고, 고유한 파이썬 패키지 집합을 가질 수 있음

> 로컬 경로에 가상의 파이썬 패키지를 설치하고 실행
>
> 프로젝트별로 관리 가능

#### 가상 환경 생성

```python
$ python -m venv <폴더명>
```

#### 가상 환경 활용

| 플랫폼 | 셀              | 가상 환경을 활성화하는 명령            |
| ------ | --------------- | -------------------------------------- |
| POSIX  | bash/zsh        | $ source \<venv>/bin/activate          |
| 윈도우 | fish            | $ source \<venv>/bin/activate.fish     |
|        | csh/tcsh        | $ source \<venv> /vin/activate.csh     |
|        | PowerShell Core | $ \<venv>/bin/Activaate.ps1            |
|        | cmd.exe         | C:\\>\<venv>\\Scripts\\activate.bat    |
|        | PowerShell      | PS C:\\>\<venv>\\Scripts\\Activate.ps1 |

#### 가상 환경 비활성화

```python
$ deactivate
```


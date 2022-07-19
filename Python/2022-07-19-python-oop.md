# 파이썬 OOP(객체지향프로그래밍)

#파이썬 #객체지향 #절차지향 #클래스 #인스턴스 



## 객체 지향 프로그래밍

- `객체(object)`는 **특정 타입**의 인스턴스(instance) 이다

  > `123, 900, 5`는 모두 **int**의 인스턴스 
  >
  > `'hello', 'bye'`는 모두 **string**의 인스턴스 
  >
  > `[232, 89, 1], []`은 모두 **list**의 인스턴스

- 객체의 특징
  - 타입 : 어떤 연산자와 조작이 가능한가?
  - 속성 : 어떤 상태(데이터)를 가지는가?
  - 조작법 : 어떤 행위(함수)를 할 수 있는가?

- 객체지향 프로그래밍이란?

  - 프로그램을 여러 개의 독립적인 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍 방법

  - 현실 세계를 프로그램 설계에 반영(추상화)

  - 프로그램을 유연하고 변경 용이하게 만들기 때문에 대규모 소프트웨어 개발에 사용

  - 개발, 보수 편리, 진관적 코드 분석 가능

    > Java, Python, C++ 등

- 절차지향 프로그래밍

  - 개체를 순차적으로 처리하여 프로그램 전체가 유기적으로 연결되어있는 프로그래밍. C언어가 대표적

  - 실행 속도 빠름

  - 유지보수 어려움

    > C언어

- 절차지향 vs 객체지향 예시

  ```python
  # 사각형 넓이 구하기
  # 사각형1 = 가로a, 세로b
  # 사각형2 = 가로c, 세로d
  
  # 절차지향_1
  a = 10
  b = 30
  squarel_area = a * b
  squarel_circumference = 2 * (a + b)
  c = 300
  d = 20
  square2_area = c * d
  square2_circumference = 2 * (c + d)
  
  # 절차지향_2_함수
  def area(x,y):
      return x * y
  def circumference(x,y):
      return 2 * (x + y)
  a = 10
  b = 30
  c = 300
  d = 20
  square1_area = area(a,b)
  square1_circumference = circumference(a,b)
  square2_area = area(c,d)
  square2_circumference = circumference(c,d)
  
  # 객체지향_클래스 내부의 함수 메서드
  class Rectangle:
      def __init__(self, x, y):
          self.x = x
          self.y = y
      
      def area(self):
          return self.x * self.y
      def circumference(self):
          return 2 * (self.x + self.y)
      
  r1 = Rectangle(10, 30)
  r1.area()
  r1.circumference()
  
  r2 = Rectangle(300, 20)
  r2.area()
  r2.circumference()
  ```

  > - 사각형 - Class
  > - 각 사각형 (R1, R2) - Instance
  > - 사각형의 정보 - 속성
  > - 사각형의 행동/기능 - Method





## OOP기초

```python
# 클래스 정의
class MyClass:
	pass
# 인스턴스 생성
my_instance = MyClass()
# 메서드 호출
my_instance.my_method()
# 속성
my_instance.my_attribute
```

> ### 표기법
>
> CamelCase : 클래스 이름에 사용. 낙타 등 처럼 울룩불룩해서
>
> snake_case : 변수 이름에 사용. 뱀처럼 바닥에 기어가서

> 객체의 틀(클래스)을 가지고, 객체(인스턴스)를 생성한다.

- ### 클래스와 인스턴스

  - 클래스 : 객체들의 분류
  - 인스턴스 : 하나하나의 실체

- ### 속성

  - 특정 데이터 타입/클래스의 객체들이 가지게 될 상태/데이터를 의미

- ### 메소드

  - 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위

  ```python
  class Person:
      
      def talk(self):
          print('안녕')
          
      def eat(self, food):
          print(f' {food}를 냠냠')
          
  personal = Person()
  personal.talk()  # 안녕
  personal.eat('피자')   # 피자를 냠냠
  ```

- ### 객체 비교하기

  - #### `==`

    - 동등한
    - 같아 보이지만 실제로 동일한 객체를 가리키고 있다고 확인하지는 못함

  - #### `is`

    - 동일한
    - 두 변수가 동일한 객체를 가리키는 경우 True

  - #### 얕은 복사 & 깊은 복사

    - ##### 얕은 복사

      - 얕은 복사 실패

      ```python
      a = [1, 2, 3]
      b = a
      b[0] = 'hi'
      
      # a
      ['hi',2,3]
      # b
      ['hi',2,3]
      ```

      > a의 메모리 주소를 그대로  b에 주었기 때문에 b를 수정하면 a도 변화한다.

      - 얕은 복사 하는 방법

      ```python
      # List 형 변환
      # -> 사실은 list인 것도, 값도 알지만 list를 통해 새로운 메모리에 할당 가능
      b = list(a)
      b[0] = 'hi'
      
      # a
      [1, 2, 3]
      # b
      ['hi',2,3]
      ```

      ```python
      # 슬라이싱
      b = a[::]
      b[0] = 'hi'
      
      # a
      [1, 2, 3]
      # b
      ['hi',2,3]
      ```

      

    - ##### 깊은 복사

      - 깊은 복사 실패

      ```python
      a = [[1,2],2,3]
      b = list(a)
      b[0][0] = 'hi'
      
      # a
      [['hi',2],2,3]
      # b
      [['hi',2],2,3]
      ```

      - 깊은 복사 하는 방법

      ```python
      import copy
      a = [[1,2],2,3]
      b = copy.deepcopy(a)
      b[0][0] = 'hi'
      
      # a
      [[1,2],2,3]
      # b
      [['hi',2],2,3]
      ```

- ### 인스턴스

  - #### 인스턴스 변수

    - 인스턴스가 개인적으로 가지고 있는 속성
    - 각 인스턴스들의 고유한 변수

  - 생성자 메소드에서 self.<name>으로 정의

  - 인스턴스가 생성된 이후 <instance>.<name>으로 접근 및 할당

  ```python
  class Person:
      
      def __init__(self, name):
          self.name = name   # 인스턴스 변수 정의
          
  john = Person('john')  # 인스턴스 변수 접근 및 할당
  print(john.name)
  #john
  john.name = 'John Kim' # 인스턴스 변수 접근 및 할당
  print(john.name)
  #John Kim
  ```

  - #### 인스턴스 메소드

    - 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메소드
    - 클래스 내부에 정의되는 메소드의 기본
    - 호출 시, 첫번째 인자로 인스턴스 자기자신이 전달됨

    ```python
    class MyClass
    	def instance_method(self, arg1, ...)
    ```

  - #### self

    - 인스턴스 자기자신
    - 파이썬에서 인스턴스 메소드는 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 설계
      - 매개변수 이름으로 self를 첫번째 인자로 정의
      - 다른 단어로 써도 작동하지만, 파이썬의 암묵적인 규칙

  - #### 생성자 메소드

    - 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드
    - 인스턴스 변수들의 초기값을 설정
      - 인스턴스 생성
      - \_\_init\_\_메소드 자동 호출

    ```python
    class Person:
        
        def __init__(self):
            print('인스턴스가 생성되었습니다.')
    personal = Person()
    # 인스턴스가 생성되었습니다.
    
    class Person:
        
        def __init__(self, name):
            print(f'인스턴스가 생성되었습니다. {name}')
    personal = Person('지민')
    # 인스턴스가 생성되었습니다. 지민
    ```

    

  - #### 소멸자 메소드

    - 인스턴스 객체가 소멸되기 직전에 호출되는 메소드

    ```python
    class Person:
        
        def __del__(self):
            print('인스턴스가 사라졌습니다.')
    personal = Person()
    del person1
    # 인스턴스가 사라졌습니다.
    ```

    
